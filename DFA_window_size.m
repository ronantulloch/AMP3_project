function M = DFA_window_size(A, k)
%This function transforms the states of a DFA to be given a set window size.

%Initialise the windows of DFA elements.
windowed_A = [];

for i = 1:length(A)
	%Grab the current element to window.
	current_element = char(A(i));

	%Make the prefixes.
	for j = 1:length(current_element)
		if length(current_element(1:j)) < k
			%Grab the firs few prefixes that are not k length.
			windowed_A = [windowed_A, string(current_element(1:j))];
		else
			%Grab the rest of the windows.
			windowed_A = [windowed_A, string(current_element(j-k+1:j))];
		end
	end
end

%Grab the DFA.
M = DFA_construct(windowed_A);
end