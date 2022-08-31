function [MI] = make_irreducible(M)
Q = M{1};
Sigma = M{2};
delta = M{3};
q_0 = M{4};
F = M{5};

if ~any(~any(delta')) % test if its already irreducible
    disp("already irreducible")
else                 % if not, make it so
    delta = [delta, zeros(size(delta,1),1)];
    for i = 1:length(Q)               
        if any(ismember(F, i)) % assumes the initial state is state 1
            delta(i,end) = 1;
        end   
    end
    Sigma = [Sigma, "rtn"]; % assumes "rtn" is not already an element of sigma
end

MI = {Q, Sigma, delta, q_0, F};
end