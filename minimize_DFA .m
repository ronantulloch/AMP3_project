function [Q_, q_0_, delta_, F_, sigma_] = minimize_DFA(Q, q_0, delta, F, sigma)
    
% Check inputs:
% Q, q_0, F are numeric arrays, q_0 and F are subsets of Q
% sigma is a character array
% delta is a numeric matrix of the correct dimensions (|Q|x|sigma|)
    
    sigma_ = sigma; % could check to make sure all words are used?
    
    
    % Totally-define the DFA
    d = delta == 0;
    d = d*(size(delta,1)+1);
    delta = delta + d;
    new_row = ones(1, size(delta,2));
    new_row = new_row*(size(delta,1)+1);
    delta = [delta; new_row];
    
    Q = [Q, max(Q)+1]; % assuming Q is finite
    
    % Group States
    % Create arrays with the index of states in each group
    pi = {};
    finals = [];
    non_finals = [];
    
    for i = 1:length(F)
        finals = [finals, find(Q == F(i))];
    end
    
    for i = 1:length(Q)
        if ~any(ismember(finals, i))
            non_finals = [non_finals, i];
        end
    end
    pi{1} = non_finals;
    pi{2} = finals;
    
    rpt = -1; % counts number of repeats, for testing
    
    % Repeat:
    %   Check each letter for each element of each group
    
    while true % will reset if need to create a new state
        rpt = rpt + 1;
        % the identity matrix defines how each *original* state moves with 
        % the new state space,
        % essentially a translation of delta from old to new states
        
        identity = zeros(length(Q), length(sigma));
        
        % create identity matrix
        for i = 1:size(identity, 1)           
            for s = 1:length(sigma)                
                for j = 1:length(pi)                   
                    if any(ismember(pi{j}, delta(i,s)))
                        identity(i,s) = j;
                    end
                end                
            end            
        end


        % go through each state in each pi{i} to see if identity rows are
        % the same
        new_states = {};
        state_identity = {};
        for i = 1:length(pi)
            for j = 1:length(pi{i})
                if j == 1
                    % set identity for the state
                    state_identity{end+1} = identity(pi{i}(j),:);
                else
                    
                    % test if state identity differs from sub-state 1
                    if any(identity(pi{i}(j),:) ~= state_identity{i}) 
                        % if so, let system know to seperate this state    
                        new_states{end+1} = [pi{i}(j), i, j]; 
                        % new states{i} = [substate number, location in pi]
                    end
  
                end
            end
        end
        num_removed = zeros(length(pi));
        % rearrange substates as needed
        if ~isempty(new_states)

            for i = 1:length(new_states) % find a new home for each substate
                
                state = new_states{i}(2); % get indices for this substate
                substate = new_states{i}(3) - num_removed(state);
                
                pi{state}(substate) = []; % remove substate from old state
                num_removed(state) = num_removed(state) + 1;
                
                for j = 1:length(pi) % create new state or add to existing equivalent state
                    
                    if ~any(~(identity(new_states{i}(1),:) == state_identity{j})) % if two ids are the same
                        
                        % make sure we do not add dead state into final states
                        if ~any(identity(new_states{i}(1),:) ~= identity(new_states{i}(1),:)) && ~any(ismember(pi{j},F)) 
                            pi{j} = [pi{j}, new_states{i}(1)]; % 
                            break % add to state j & move on to next new substate
                        end
                        
                    end
                    
                    if j == length(state_identity) % if it cant find a home          
                        
                        pi{end+1} = new_states{i}(1); % create new state                        
                        state_identity{end+1} = identity(new_states{i}(1),:); 
                    end
                end
            end
            
        else % if no new states to add, do not cycle again
            break
        end      
    end      % will loop again if any new states created

    Q_ = 1:length(pi); % redefine states to be consecutive number

    
    % Create new delta for new state set
    delta_ = [];
    for i = 1:length(pi)
        delta_ = [delta_; state_identity{i}];        
    end  
    
    
    % Create new final state set
    F_ = [];
    for f = 1:length(F)
        for i = 1:length(pi)
            
            if any(ismember(pi{i}, F(f))) && ~any(ismember(F_, i))
                F_ = [F_, i];
            end
            
        end
    end
    

    % Remove dead state set if there is one
    for i = 1:length(pi)
        
        current_state_id = state_identity{i};
        
        % test if state goes only to itself and is not a final state
        if ~any(current_state_id ~= current_state_id(1)) && ~any(ismember(F_, i))
                        
            Q_(i) = []; %remove state from Q
            Q_ = 1:length(Q_); %redefine states
            
            %modify delta
            delta_(i,:) = []; %                      remove dead row i
            delta_ = delta_- i*ismember(delta_,i); % change i to 0 in delta
            pi(i) = [];
        end
    end
    
    % Create the new initial state set
    
    q_0_ = [];
    for q = 1:length(q_0)
        for i = 1:length(pi)
            if any(ismember(pi{i}, q)) && ~any(ismember(q_0_, q))
                q_0_ = [q_0_, i];
            end
        end
    end
    
    disp("number of repeats: " + rpt)
end