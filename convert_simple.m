function [MC] = convert_simple(M)
Q = M{1};
Sigma = M{2};
delta_old = M{3};
q_0 = M{4};
F = M{5};

Q = double(Q(1,:));
F = double(F(1,:));
q_0 = double(q_0(1));

delta = zeros(length(Q), length(Sigma));

letters = 1:length(Sigma);

for i = 1:size(delta_old, 1)
    row = double(delta_old(i,1));
    col = letters(Sigma == delta_old(i,3));

    delta(row,col) = double(delta_old(i,4));
end
 
MC = {Q, Sigma, delta, q_0, F};
end