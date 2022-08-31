function [Q, Sigma, delta, q_0, F] = transform(Q, Sigma, delta, F)
%Transform Q
Q = double(Q(1,:)) + 1;

%Transform q_0
q_0 = 1; %By definition

%Transform F
F = double(F(1,:)) + 1;

%Transform delta
new_delta = zeros(length(Q),length(Sigma));
for i = 1:length(Q) % along rows of new delta
    for j = 1:length(Sigma) % along columns of new delta
        for d = 1:length(delta) % for all known transitions
            % If that transition starts at Q(i) and uses character Sigma(j)
            if (double(delta(d,1)) == Q(i)) && (delta(d,3) == Sigma(j))
                % Add transition to the state transitioned to
                new_delta(i,j) = double(delta(d,4));
            end
        end
    end
end
% Replace
delta = new_delta;

end