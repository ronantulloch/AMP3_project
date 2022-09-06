Event_Log_1 = ["card", "cab", "dar", "dab"];
Event_Log_2 = ["card", "cab", "dab", "dbc", "acb"];

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
% look at what each state represents
states = state_list(M4)

% Calculate precision & recall for M4
[p1,r1] = precall(M4,Event_Log_1)
[p2,r2] = precall(M4,Event_Log_2)

% how about for the irreducible versions of M4 and L
[p1,r1] = precall_irr(M4,Event_Log_1)
[p2,r2] = precall_irr(M4,Event_Log_2)