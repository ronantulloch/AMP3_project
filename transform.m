function [Q, Sigma, delta, q_0, F] = transform(Q, Sigma, delta, F)
%Transform Q
Q = double(Q(1,:)) + 1

%Transform q_0
q_0 = 1 %By definition

%Transform F
F = double(F(1,:)) + 1

%Transform delta

for i = 1:length(Q)


end

%Transform delta

end