import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import svds


def is_int(string):
    """ True if given string is int else False"""
    try:
        return int(string)
    except ValueError:
        return False


genotype_data = []
with open('sparse_survival_time_genotype_1663.dat', 'r') as f:
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

#! To use TrancatedSVD, the data should be rearranged s.t. 
#! each column corresponds to a feature.

G = coo_matrix((data, (row, col)), shape=(M, N), dtype=np.float64)

num_components = 100


#! do SVD for G s.t.
#! G = U*S*V^t, U in M * k, S is k * k and V is k * N
U, S, Vt = svds(G, k = num_components)

X = np.diag(S) @ Vt

np.savetxt('truncated_svd.csv', X, delimiter = '\t')