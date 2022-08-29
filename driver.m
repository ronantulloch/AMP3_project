clc;
%Get all output in a text file.
dfile = 'output.txt';
if exist(dfile, 'file') ; delete(dfile); end
diary(dfile)
diary on

% %Clean the chosen file.
% executed = system("R CMD BATCH manipulating.R"); %Try not to run too often as this script takes too long.

Event_Log =  ["car", "cab", "dar", "dab"]; %Later turn this into READ CSV.

%Get the DFA from the event log.
[Q, Sigma, delta, q_0, F] = DFA_construct(Event_Log);

%Get the transition matrix from the DFA.
P = DFA_to_markov(delta, Event_Log);

%Minimise the DFA
[Q, Sigma, delta, q_0, F] = transform(Q, Sigma, delta, F); %Transform 
diary off
