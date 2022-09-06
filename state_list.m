function Q_list = state_list(M)
% Input: 
%   M: a simple form DFA
% Output:
%F_list: a string array

sigma = M{2};
delta = M{3};
q_0 = M{4};
F = M{5};

rows = 1:size(delta,1);
rows = rows';
rows = repmat(rows,1,size(delta,2));

if any(delta == rows, 'all')
    disp("Cycles present: returning first set of final states")
end
Q = cell(1,size(delta,1));

for f = 1:length(q_0) % create traces from each initial state
    states = q_0(f); 
    Q{states(1)} = ""; 
    
    while ~isempty(states) % write states until end of trace
        for j = 1:size(delta,2)

            if delta(states(1),j) ~= 0

                next_state = delta(states(1),j);
                prev_state = states(1);
                next_letter = sigma(j);
                Q{next_state} = [Q{next_state}, strcat(Q{prev_state}, next_letter)];

                states = [states, next_state];
                
            end
         end

        states(1) = [];
     end


end
    

for i = 1:length(Q)
    Q{i} = unique(Q{i});
end

Q_list = Q;
end