function [Q, Sigma, delta, q_0, F] = transform(Q, Sigma, delta, F)
%Transform Q
Q = double(Q(1,:)) + 1

%Transform q_0
q_0 = (double(delta(delta(:,2) == "", 4))') + 1

%Transform F
F = double(F(1,:)) + 1

%Transform delta



%Transform delta

end