clear;
X = readmatrix("RawX.xlsx");
n = size(X, 1);
[U, S, V] = svd(X);
format long;
s = [];
for i = 1:n
    s(i) = S(i, i);
end

s(1:10)

writematrix(s, 'raw_singular_value.xlsx');

% 
% fprintf("the max difference of full svd is ");
% max(max(abs(U*S*V' - X)))
% for k = 5:10 
%     fprintf("the max difference of %d-svd is ", k);
%     max(max(abs(U(1:n, 1:k)*S(1:k, 1:k)*V(1:n, 1:k)' - X)))
% end

clear;
X = readmatrix("PreprocX.xlsx");
n = size(X, 1);
[U, S, V] = svd(X);
s = [];
for i = 1:n
    s(i) = S(i, i);
end
s(1:10)
writematrix(s, 'preproc_singular_values.xlsx');

% fprintf("the max difference of full svd is ");
% max(max(abs(U*S*V' - X)))
% for k = 5:10 
%     fprintf("the max difference of %d-svd is ", k);
%     max(max(abs(U(1:n, 1:k)*S(1:k, 1:k)*V(1:n, 1:k)' - X)))
% end

