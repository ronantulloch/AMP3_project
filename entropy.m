function [ent] = entropy(M)
% Input:
%   A simple form DFA

    MI = make_irreducible(M);
    delta = MI{3};
    transition = delta_to_transition(delta);
    ent = log2(max(real(eig(transition))));
end