clc;
%Load in the data.
A = readtable("CSV_Files/bpi_challenge_2013_incidents.csv");
A = string(table2cell(A)); A = A';
A = A(1:100);

% A = ["cab", "car", "dadb", "dar", "acc"];

%Construct the sequence based DFA
M_1 = DFA_construct(A);

%Multiset Based DFA
M_2 = DFA_construct_MULTI(A);

%Set Based DFA
M_3 = DFA_construct_SET(A);

%Set the k window.
k = 3;

%Get the windowed DFAs
M_1w = DFA_window_size(M_1, k, 0);
M_2w = DFA_window_size(M_2, k, 1);
M_3w = DFA_window_size(M_3, k, 0);

%Visualise the windowed DFA.
% DFA_vis(M_1)
% DFA_vis(M_2)
% DFA_vis(M_3)
% DFA_vis(M_1w)
% DFA_vis(M_2w)
DFA_vis(M_3w)

% %Get the irreducible markov distribution.
P = DFA_to_markov(M_2w, A)
