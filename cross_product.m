function [M3] = cross_product(M1, M2)
% Inputs:
%   M1 of the form {Q, Sigma, delta, q_0, F} Expanded Form **
%   M2 of the form {Q, Sigma, delta, q_0, F} Expanded Form **
% Output:
%   M3 = {Q3, Sigma, delta3, q_3, F3} Expanded Form **

% test inputs
if size(M1{5}, 1) ~= 2
    disp("Wrong format, please input an expanded form DFA")
    return
end

F1 = M1{5}; F2 = M2{5};
F3 = intersect(F1(2,:), F2(2,:)); 
M3 = DFA_construct(F3);

end