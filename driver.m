Event_Log_1 = ["card", "cab", "dar", "dab"];
Event_Log_2 = ["carb", "cab", "dab", "dbc", "acb"];

%Get the DFAs from the event log.

% M1
M1 = DFA_construct(Event_Log_1);
% M2
M2 = DFA_construct(Event_Log_2);

% M3 = M1 x M2
M3 = cross_product(M1, M2);

% Minimize M3, call it M4
M4 = minimize_DFA(M3)

% have a look at the minimal delta of M1 x M2
M4{3}

% Look at the entropy of M4 (or rather the irreducible equivalent of M4)
entropy(M4)

