clc;
%Load in the data.
% A = readtable("CSV_Files/bpi_challenge_2013_incidents.csv");
% A = string(table2cell(A)); A = A';
% A = A(1:100);

A = ["cab", "car", "dadb", "dar", "acc"];

%Construct the sequence based DFA
M = DFA_construct_MULTI(A)

% %Set the k window.
% k = 3;
% 
% %Get the windowed DFA
% M_windowed = DFA_window_size(M, k);
% 
% %Visualise the windowed DFA.
% DFA_vis(M_windowed)
% 
% %Get the irreducible markov distribution.
% P = DFA_to_markov(M_windowed, A);
