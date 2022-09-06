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

MnL = intersect(L,F_list);
M1 = DFA_construct(MnL); M1 = minimize_DFA(M1);
M2 = DFA_construct(L); M2 = minimize_DFA(M2);
M3 = DFA_construct(F_list); M3 = minimize_DFA(M3);

e1 = entropy(M1); e2 = entropy(M2); e3 = entropy(M3);

p = e1/e3;
r = e1/e2;

end