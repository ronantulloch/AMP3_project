function [M] = DFA_construct_MULTI(A)
%Make a prefix tree of the event DFA with no repeats.
M = DFA_construct(A);

%Grab some useful information out of the model.
Q = M{1};
delta = M{3};
F = M{5};

for i = 1:size(Q,2)
	current_Q = Q(i);

	for j = 1:size(Q,2)
		if string(sort(char(current_Q))) == string(sort(char(Q(j))))
			Q(1,j) = Q(1,i);
		end
	end


	for j = 1:size(F,2)
		if Q(2,i) == F(2,j)
			F(1,j) = Q(1,i);
		end
	end

	for j = 1:size(delta,1)
		if delta(j,2) == Q(2,i)
			delta(j,1) = Q(1,i);
		end
		if delta(j,5) == Q(2,i)
			delta(j,4) = Q(1,i);
		end
	end
end

delta = unique(delta, "rows", "stable");


M{6} = A;
end