function [p,r] = precall(M, L)
% Inputs:
%   M: A DFA (cell array)
%   L: An event log (string array)
% Output:
%   The precision of the model M on the log L

if size(M{1},1) ~= 1 % convert to simple form if needed
    M = convert_simple(M);
end
Q = M{1}; sigma = M{2}; delta = M{3}; q_0 = M{4}; F = M{5};

Q_list = state_list(M);
F_list = [];
for i = 1:length(F)
    F_list = [F_list, Q_list{F(i)}];
end


MnL = intersect(L,F_list);
p = length(MnL)/length(F_list);
r = length(MnL)/length(L);

end