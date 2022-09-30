function P = DFA_to_markov(M, A)
%%This code takes a valid DFA and calculates a corresponding transition markov chain
%%transition matrix. See read me for output format.

%Grab transition matrix out of the model
delta = M{3};

%Get the required size of the matrix
dim = max(double(delta(:,4))) + 1;

%Initialise the transition matrix
P = zeros(dim);

%Get the number of transitions from the initial state.
q_0_size = length(A);

%Consider each transition
for i = 1:size(delta, 1)

	%Initialise the counts of the old and new transitions.
	prefix = delta(i,2);
	transition = strcat(delta(i,2), delta(i,3));

	%Get the counts of each prefix and transition in each event.
	pre_count = 0;
	post_count = 0;

	%Get the number of times the prefix and the transition appears in each event log.
	for j = 1:length(A)
		pre_count = pre_count + length(strfind(A(j), prefix));
		post_count = post_count + length(strfind(A(j), transition));
	end

	%Calculate the transition probabilities.
	%Check for the first row of the matrix.
	if prefix == ""
		post_count = 0; %Initialise the post count.

		%Count the number of observations of Sigma element.
		for j = 1:length(A)
			current_event = char(A(j));
			if transition == current_event(1)
				post_count = post_count + 1;
			end
		end

		%Calculate transition probability.
		P(str2double(delta(i,1)), str2double(delta(i, 4))) =  post_count/q_0_size;

	%If there are enough observations of the prefix then calculate transition probability.
	elseif pre_count > 0
		P(str2double(delta(i,1)), str2double(delta(i, 4))) =  post_count/pre_count;
	end
end

%Fix the transitions.
for i = 1:(size(P,1) - 1)
	if sum(P(i,:)) ~= 1
		P(i,end) = 1 - sum(P(i,:));
	end
end

%Add the escape from the end state back to the starting state.
P(end,1) = 1;

end
