import numpy as np
from scipy.sparse import coo_matrix


def is_int(string):
    """ True if given string is int else False"""
    try:
        return int(string)
    except ValueError:
        return False


genotype_data = []
with open('sparse_relapse_genotype_338.dat', 'r') as f:
    d = f.readlines()
    for i in d:
        k = i.rstrip().split("\t")
        genotype_data.append([int(i) if is_int(i) else i for i in k])
f.close()

origin_data = np.array(genotype_data, dtype='O')

row = origin_data[:, 0] - 1
data = origin_data[:, 2]

M = max(row) + 1  # M = 18926217
print('M =', M)


# to remove the blank columns
origin_col = origin_data[:, 1]
set_col = list(set(origin_col))
col = []
for i in range(len(row)):
    index = set_col.index(origin_col[i])
    col.append(index)
col = np.array(col)
N = max(col) + 1  # N = 1663
print('N =', N)

# print(len(row), len(col), len(data))

G = coo_matrix((data, (row, col)), shape=(M, N), dtype=np.float64)
ones = np.matrix(np.full((N, 1), 1))
g_ones = G @ ones  # u is the vector of mean
u = g_ones / N


# G^T G - 1 (u^T G) - (G^T u)1^T + 1(u^T u)1^T
# gt_g = G.transpose() @ G
# gt_u = G.transpose() @ u
# one_ut_g = ones @ gt_u.transpose()
# gt_u_onet = gt_u @ ones.transpose()
# ut_u = u.transpose() @ u
# one_ut_u_onet =  (ones @ ones.transpose()) * ut_u[0,0]
# cov_mat = gt_g - one_ut_g - gt_u_onet + one_ut_u_onet



# The following is from [Price et al. 2006]:
# Price et al. Nature Genetics 2006 Vol. 38 Issue 8 Pages 904-909

# G^T P^2 G - G^T P^2 u 1^T - 1 u^T P^2 G + 1 u^T P^2 u 1^T

p = (g_ones + 1)/(2 + 2*N)
for i in range(M):
    p[i, 0] = 1/(p[i, 0]*(1-p[i, 0]))

# the following P is indeed P^2 in [Price et al. 2006]
P = coo_matrix((list(p[i, 0] for i in range(M)), (np.array(range(M)), np.array(range(M)) )), shape = (M, M), dtype=np.float64)

print("P is constructed.")

p_g = P @ G
gt_p = p_g.transpose()
gt_p_g = G.transpose() @ p_g

print("the 1st part computation completes.")

gt_p_u = gt_p @ u
gt_p_u_onet = gt_p_u @ ones.transpose()

print("the 2nd part computation completes.")

ut_p = u.transpose() @ P
ut_p_u = ut_p @ u
one_ut_p_u_onet = (ones @ ones.transpose()) * ut_p_u[0,0]
print("the 3rd part computation completes.")

cov_mat = gt_p_g - gt_p_u_onet - gt_p_u_onet.transpose() + one_ut_p_u_onet
print("covariance matrix computation completes.")

np.savetxt('preproc_cov_mat.csv', cov_mat, delimiter = '\t')

