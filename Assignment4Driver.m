clc;
%Load in the data.
% A = readtable("CSV_Files/bpi_challenge_2013_incidents.csv");
% A = string(table2cell(A)); A = A';

A = ["cab", "car", "dadb", "dar"];

%Construct the sequence based DFA
M = DFA_construct(A);

%Set the k window.
k = 1;

%Get the windowed DFA
M_windowed = DFA_window_size(M, k);

%Visualise the windowed DFA.
DFA_vis(M_windowed)
