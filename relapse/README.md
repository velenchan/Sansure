
# For 1k samples
## `ICGC.mutation.genotype.1000.donor_rows`
- sample id, totally $1000$ samples

## `ICGC.mutation.genotype.1000.sparse`
- genotype data for $1000$ samples
- $3822299$ SNPs
- SNPs have only two different value, i.e., $0$ and $1$
- We can read this file into a matrix $G= (g_{i, j})$ with size $3822299 \times 1000$. For example, the first line of this file is `1  952 1`, which means that $g_{1, 952} = 1$.

## `ICGC.mutation.genotype.donor.penotype.relapse`

- classifications of relapse for the $1000$ samples, i.e., the labels
- each sample is classified as one of five categories, i.e., `1`, `2`, `3`, `4`, and `null`, where `null` can be seen as `0` (i.e., without relapse) or the corresponding sample is useless ($\color{red} to\ be\ confirmed$)

## sparse_relapse_genotype_1000.dat
The relapse label for $103$ samples. (Only $103$ out of $1000$ has labels for relapse.) The data is represented as $A\in\mathbb{R}^{M\times N}$ with $M=3822299$ and $N=103$.

## RawX.xlsx
Directly compute $X = A^TA$ for PCA, which is saved as `RawX.xlsx`.

## PreprocX.xlsx
Following the method presented in [1], we preprocess the genotype matrix as $B$, which is of the same size of $A$. Then we compute $X = B^TB$ for PCA, which is saved as `PreprocX.xlsx`.

# For 3k samples

## sparse_relapse_genotype_338.zip
The genotype data for 3k samples. There are only $338$ effective samples out of 3k for relapse, i.e., $N=338$.  Note that $M = 1892,6216$ for 3k samples.

## relapse_label_338.dat
The labels for $338$ out of 3k samples.

## covariance_matrix.py

The python code to compute the covariance matrix of the input genotype data for relapse with 3k samples. 

## preproc_cov_mat.zip

The computed covariance matrix is of size $338\times 338$.

# Method

Recall that the original $A$ has size $M\times N$. Assume that the rank of $A$ is $r$, and that the Singular Value Decomposition (SVD) of the original matrix is $A = USV^T$, where $U\in\mathbb{R}^{M\times M}$ is an orthogonal matrix, $S$ is a $M\times r$ diagonal matrix, and $V$ is a $N\times r$ matrix with each column orthogonal to each other. Suppose that we only take the first $k$ components. Then $$X  = A^TA = VS^2V^T \approx V_k S_k^2V_k^T.$$ If we consider $Y = S_kV_k^T\in \mathbb{R}^{k\times N}$ as the data with reduced dimension, then we obtain a data set with $N$ samples, each of them with $k$ features.

`Remark 1`: Note that $Y\neq S_k^2V_k^T$, but $Y = S_kV_k^T$.

`Remark 2`: From now on, $Y = S_kV_k^T$ is the new data, which only have $k$ feautures, and still have $N$ samples. We train and test different models with $Y$, not the original $A$ or $B$.

# Todo list

~~1. genotype 数据是按照 sample id 的顺序给出的，如果将没有标签的视为无效数据，则需要将相应的基因型数据删除。~~

~~2. 对于清理以后的数据进行降维处理。采用的具体降维方法，需要根据所选择的模型来确定。~~

3. 以 $Y$ 为新数据，尝试不同分类分类方法，例如朴素贝叶斯分类、决策树 (ID3, C4.5， C5.0 等)、k-近邻、神经网络等。

`注：`  剔除无效数据后，仅有~103~个有效样本，这可能会影响建模效果，不过现在我们重在走通方法.

[1] Nature Genetics 2006 Vol. 38 Issue 8 Pages 904-909 DOI: 10.1038/ng1847