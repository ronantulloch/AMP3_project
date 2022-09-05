% Function to construct DFAs using multiset prefixes
function [Q, Sigma, delta, q_0, F] = multiset(event_log)
% will include the multisets of symbols in Q to compare; will remove at end

% constructing the alphabet from event log
Sigma = (strjoin(event_log, "")); % turn the event log into a single long string
Sigma = unique(split(Sigma, ""))'; % split into individual characters, take unique characters
Sigma = Sigma(Sigma ~= ""); %Remove the empty strings at the start and end of the alphabet.

% Set state 0 as initial, empty state
q_0 = "";

% Initialise Q
Q = q_0;

% Initialise delta
delta = strings(1,3);

% Initialise final states
F = [];

% Get intermediate states and transitions
for i = 1:length(event_log)
    % Get current event
    current_event = char(event_log(i));
    for j = 1:length(current_event)
        % Get current prefix
        current_prefix = current_event(1:j);
        % sort so that elements are in order of alphabet
        current_prefix_ordered = "";
        for s = 1:length(Sigma)
            for k = 1:length(strfind(current_prefix,Sigma(s)))
                current_prefix_ordered = strcat(current_prefix_ordered,Sigma(s));
            end
        end
        % Check if sorted prefix is already in Q
        already_in_Q = 0;
        for q = 1:length(Q)
            if Q(q) == current_prefix_ordered
                already_in_Q = 1;
                % get index of this state in Q
                index_current = q;
            end
        end
        if already_in_Q == 0
            % add prefix as a state
            Q = [Q,current_prefix_ordered];
            % get index of this state in Q
            index_current = length(Q);
        end

        % ADDING TRANSITION:
        % find index of previous prefix in Q
        previous_prefix = current_prefix(1:(end-1));
        previous_prefix_ordered = "";
        for s = 1:length(Sigma)
            for k = 1:length(strfind(previous_prefix,Sigma(s)))
                previous_prefix_ordered = strcat(previous_prefix_ordered,Sigma(s));
            end
        end
        for q = 1:length(Q)
            if Q(q) == previous_prefix_ordered
                % get index of this state in Q
                index_previous = q;
            end
        end

        % add transition on the last character of the prefix
        new_transition = [string(index_previous),string(current_prefix(end)),string(index_current)];
        % checking whether it is already there
        if ~ismember(delta,new_transition,'rows') %any
            delta = [delta;new_transition];
        end
    end
    % Add last element of event log to finishing states
    % at this point, index_current will be the index in Q of state at the
    % end of the current event log
    F = [F, double(index_current)];
end
% De-duplicate F
F = unique(F);
% Change Q and q_0 to just lists of state numbers rather than multisets
Q = 1:length(Q);
q_0 = 1;
end
