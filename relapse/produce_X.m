clear;

load sparse_relapse_genotype_1000.dat;
A = spconvert(sparse_relapse_genotype_1000);
G = full(A); % Here G is a M * N matrix
G(:, all(G == 0)) = []; % remove all zero columns from G
dims = size(G);
M = dims(1); % M = 3*10^6 +
N = dims(2); % N = 400+


X = G' * G;

writematrix(X, 'RawX.xlsx');

% Preprocessing the SNP data 
%
% Principal components analysis corrects for stratification in genome-wide association studies
% A. L. Price, N. J. Patterson, R. M. Plenge, M. E. Weinblatt, N. A. Shadick and D. Reich
% Nature Genetics 2006 Vol. 38 Issue 8 Pages 904-909
% DOI: 10.1038/ng1847

for i = 1:M
    s = sum(G(i, 1:N));
    u = s/N;
    p = (1+s)/(2+2*N);
    G(i, 1:N) = G(i, 1:N) - u; % To make the sum of each row zero
    G(i, 1:N) = G(i, 1:N)/sqrt(p*(1-p)); % normalize row i 
end

X = G' * G;
clear("G");
%clear("A");
writematrix(X, 'PreprocX.xlsx');



