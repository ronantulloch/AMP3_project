function [M] = DFA_construct_MULTI(A)
%Make a prefix tree of the event DFA with no repeats.
M = DFA_construct(A);

%Grab some useful information out of the model.
Q = M{1};
delta = M{3};
F = M{5};

%Place the transition function back into the model.
for i = 1:size(delta,1)
	delta(i,2) = string(sort(char(delta(i,2))));
	delta(i,5) = string(sort(char(delta(i,5))));
end

for i = 1:size(Q,2)
	Q(2,i) = string(sort(char(Q(2,i))));
end

for i = 1:size(F,2)
	F(2,i) = string(sort(char(F(2,i))));
end


%Remove duplicates and place back into the model.
[~, IA] = unique(delta(:,[2,3,5]),"rows");
delta = delta(IA,:);
Q = (unique(Q',"rows"))';
F = (unique(F',"rows"))';
M{3} = sortrows(delta,1);
M{1} = Q;
M{5} = F;
end