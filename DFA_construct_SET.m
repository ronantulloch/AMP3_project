function [M] = DFA_construct_SET(A)

set_events = [];
log = ["";""];

%Check every event log
for i = 1:length(A)

    %Set the current event as a character array.
    current_event = char(A(i));
    %Set the current set equivalent of the DFA
    set_event = char([]);

    %Check for duplicate entries in the character array.
	for j = 1:length(current_event)
		if ~any(contains(string(set_event), string(current_event(j))))
			%Add the set of events.
            set_event = [set_event, current_event(j)];

		else
			log_current = [string(set_event); string(current_event(j))];
			log = [log, log_current];
		end
		
	end
    set_events = [set_events, string(set_event)];
end

%Remove empty string.
log = unique(log(:,2:end)', "rows");

%Make a prefix tree of the event DFA with no repeats.
M = DFA_construct(set_events);
Q = M{1};
delta = M{3};

for i = 1:size(log,1)
	state_no = Q(1, log(i) == Q(2,:));

	new_delta = [state_no, log(i,1), log(i,2), state_no, log(i,1)];
	delta = [delta; new_delta];
end

M{3} = sortrows(delta);

end