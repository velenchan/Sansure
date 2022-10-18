Suppose that $G = (g_{i,j})$ is the $3822299 \times 1000$ matrix for genotype.

Since only $457$ samples out of $1000$ has lables for survival time, we remove the other $543$ samples.

Now the genotype matrix is a $M\times N \, ( = 3822299 \times 457)$ matrix $A = (a_{i,j})$.


# survival_time_label.dat
The survival time for these $457$ samples.

# RawX.xlsx
Directly compute $X = A^TA$ for PCA, which is saved as `RawX.xlsx`.

# PreprocX.xlsx
Following the method presented in [1], we preprocess the genotype matrix as $B$, which is of the same size of $A$. Then we compute $X = B^TB$ for PCA, which is saved as `PreprocX.xlsx`.

# Method

Recall that the original $A$ is of $M\times N$. Assume that the rank of $A$ is $r$, and that the Singular Value Decomposition (SVD) of the original matrix is $A = USV^T$, where $U\in\mathbb{R}^{M\times M}$ is an orthogonal matrix, $S$ is a $M\times r$ diagonal matrix, and $V$ is a $N\times r$ matrix with each column orthogonal to each other. Suppose that we only take the first $k$ components. Then $$X  = A^TA = VS^2V^T \approx V_k S_k^2V_k^T.$$ If we consider $Y = S_kV_k^T\in \mathbb{R}^{k\times N}$ as the data with reduced dimension, then we obtain a data set with $N$ samples, each of them with $k$ features.

`Remark 1`: *Note that $Y\neq S_k^2V_k^T$, but $Y = S_kV_k^T$.*

[1] Nature Genetics 2006 Vol. 38 Issue 8 Pages 904-909 DOI: 10.1038/ng1847