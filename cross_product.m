function [M3] = cross_product(M1, M2)
% Inputs:
%   Two DFAs M1 & M2
% Output:
%   M3 = {Q3, Sigma, delta3, q_3, F3} Expanded Form **

if size(M1{1},1) ~= 1 % convert to simple form if needed
    M1 = convert_simple(M1);
end
if size(M2{1},1) ~= 1 % convert to simple form if needed
    M2 = convert_simple(M2);
end
F1 = M1{5}; F2 = M2{5};

Q_list1 = state_list(M1);
F_list1 = [];
for i = 1:length(F1)
    F_list1 = [F_list1, Q_list1{F1(i)}];
end
Q_list2 = state_list(M2);
F_list2 = [];
for i = 1:length(F2)
    F_list2 = [F_list2, Q_list2{F2(i)}];
end

F_list = intersect(F_list1,F_list2);
M3 = DFA_construct(F_list);
M3 = convert_simple(M3);
end