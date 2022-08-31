function [transition] = delta_to_transition(delta)

    Q = size(delta, 1);

    transition = zeros(Q,Q);
    
    for i = 1:Q
        for s = 1:size(delta,2)
            for j = 1:Q
                if delta(i,s) == j
                    
                    transition(i,j) = transition(i,j) + 1;
                    
                end
            end
        end
    end
end