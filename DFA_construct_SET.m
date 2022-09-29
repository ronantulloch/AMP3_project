function [M] = DFA_construct_SET(A)

%Initialise the set version of the events and the log of repeats.
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
			%Add to an event in set form
            set_event = [set_event, current_event(j)];

		else
			%Add the set event that repeats.
			log_current = [string(set_event); string(current_event(j))];
			log = [log, log_current];
		end
		
	end
	%Group all of the set defined events.
    set_events = [set_events, string(set_event)];
end

%Remove empty string and grab unique.
log = unique(log(:,2:end)', "rows");

%Make a prefix tree of the event DFA with no repeats.
M = DFA_construct(set_events);

%Grab some useful information out of the model.
Q = M{1};
delta = M{3};

for i = 1:size(log,1)
	%Get the state number at which the trace cycles.
	state_no = Q(1, log(i) == Q(2,:));
	
	%Construct a new transition and add to the transition function.
	new_delta = [state_no, log(i,1), log(i,2), state_no, log(i,1)];
	delta = [delta; new_delta];
end

%Place the transition function back into the model.
M{3} = sortrows(delta,1)
end