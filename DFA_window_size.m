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

%Remove and number the duplicate Q values.
Q = sortrows(unique(Q(2,:)'))';
Q(2,:) = Q(1,:);
Q(1,:) = string(1:size(Q,2));


for i = 1:size(Q,2)
	current_Q = Q(2,i);

	for j = 1:size(F,2)
		if current_Q == F(2,j)
			F(1,j) = Q(1,i);
		end
	end

	for j = 1:size(delta,1)
		if current_Q == delta(j,2)
			delta(j,1) = Q(1,i);
		end
		if current_Q == delta(j,5)
			delta(j,4) = Q(1,i);
		end
	end

end

delta = unique(delta, "rows")


%Place back into the model
M{1} = Q;
M{3} = delta;
M{5} = F;
end
