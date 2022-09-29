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

%Place the new delta back into the model.
delta_temp = delta(:, [2,3,5]);
[~, IA] = unique(delta_temp, 'rows');

M{3} = delta(IA,:)

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

%Place back into the model
M{1} = Q;
M{5} = F;

end