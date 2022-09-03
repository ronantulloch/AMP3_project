function [M] = DFA_construct_SET(A)

set_events = [];
log = [];

%Check every event log
for i = 1:length(A)

    %Set the current event as a character array.
    current_event = char(A(i));
    %Set the current set equivalent of the DFA
    set_event = char([]);

    %Check for duplicate entries in the character array.
    for j = 1:length(current_event) - 1
        if current_event(j) ~= current_event(j+1)
            set_event = [set_event, current_event(j)];

		else 
			%Log the repeats in the event log.
			log = horzcat(log, string([set_event, current_event(j)]));
        end
	end
	%Add the last digit and add to the version of the 
	set_event = [set_event, current_event(end)];
    set_events = [set_events, string(set_event)];
end

%Remove empty string.
log = unique(log(log~=""))

%Make a prefix tree of the event DFA with no repeats.
M = DFA_construct(set_events);


%Let's add the set transitions for the transition function
delta = M{3};
for i = 1:length(log)
	delta_temp = delta(delta(:,2) == log(i),:);

	if any(log(i) == set_events)
		delta_temp = delta(delta(:,5) == log(i),:);
		beta = delta_temp;

		final_element = char(beta(5));
		final_element = final_element(end);

		beta(3) = final_element;
		beta(1) = beta(4);
		beta(2) = beta(5);

		delta = [delta; beta];

	else
		for j = 1:size(delta_temp, 1)
		%Grab final element
		final_element = char(delta_temp(j,2));
		final_element = final_element(end);

		%Construct the cycle
		beta = delta_temp(j,:);
		beta(3) = final_element;
		beta(5) = beta(2);
		beta(4) = beta(1);
		delta = [delta; beta];
	end

	end
	
end

%Add the transition back in.
M{3} = sortrows(unique(delta, 'rows'));

end