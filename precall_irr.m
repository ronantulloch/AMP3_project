function [p,r] = precall_irr(M, L)
% Inputs:
%   M: A DFA (cell array)
%   L: An event log (string array)
% Output:
%   The precision & recall of the model M on the log L

if size(M{1},1) ~= 1 % convert to simple form if needed
    M = convert_simple(M);
end
F = M{5};

Q_list = state_list(M);
F_list = [];
for i = 1:length(F)
    F_list = [F_list, Q_list{F(i)}];
end

ML = DFA_construct(L); ML = minimize_DFA(ML);
MMnL = cross_product(M, ML);

e1 = entropy(MMnL); e2 = entropy(ML); e3 = entropy(M);

p = e1/e3;
r = e1/e2;

end