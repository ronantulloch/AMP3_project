function M = DFA_window_size(M, k)
%This function transforms the states of a DFA to be given a set window size.

%Grab the transition array.
delta = M{3};

for i = 1:size(delta, 1)
	%Get the state identifiers as character arrays
	first_state = char(delta(i,2));
	second_state = char(delta(i, 5));

	%If the state identifier is long enough take the window and place back into delta.
	if ~(length(first_state) < k)
		new_first_state = string(first_state((end-k+1):end));
		new_second_state = string(second_state((end-k+1):end));
		delta(i,2) = new_first_state;
		delta(i,5) = new_second_state;
	end
end

%Truncate the states.
Q = M{1};
for i = 1:size(Q,2)
	current_element = char(Q(2,i));
	if length(current_element) > k
		Q(2,i) = string(current_element(end-k+1:end));
	end
end
F = M{5};
for i = 1:size(F,2)
	current_element = char(F(2,i));
	if length(current_element) > k
		F(2,i) = string(current_element(end-k+1:end));
	end
end

%Merge entries in the Q, F and delta functions.
for i = 1:size(Q,2)
	%Select the current state.
	indexes = [];
	current_Q = Q(2,i);

	%Replace all of the indexes.
	for j=1:size(Q,2)
		if current_Q == Q(2,j)
			indexes = [indexes, Q(1,j)];
		end
	end

	%Get the minimum state.
	min_state = string(min(double(indexes)));
	indexes = indexes(indexes~=min_state);

	%Replace the final states.
	for k = 1:size(F,2)
		if any(F(1,k)==indexes)
			F(1,k) = min_state;
		end
	end

	%Replace the total states.
	for k = 1:size(Q,2)
		if any(Q(1,k)==indexes)
			Q(1,k) = min_state;
		end
	end

	%Replace the deltas
	for k = 1:size(delta,1)
		if any(delta(k,1)==indexes)
			delta(k,1) = min_state;
		end
	end
		for k = 1:size(delta,1)
		if any(delta(k,4)==indexes)
			delta(k,4) = min_state;
		end
	end
end

%Remove duplicates
Q = unique(Q', 'rows'); Q = Q';
F = unique(F', 'rows'); F = F';
delta = unique(delta, "rows");

%Place back into the model
M{1} = Q;
M{3} = delta;
M{5} = F;
end