% DFA MINIMIZATION

% An example DFA
%Q = ["", "c", "d", "ca", "da", "cab", "car", "dab", "dar"]; is the langague
Q  = [1, 2, 3, 4, 5, 6, 7, 8, 9]; 
q_0 = [2,3];
%F = ["car", "cab", "dar", "dab"];
F  = [6,7,8,9];
delta = [0 0 2 3 0;
         4 0 0 0 0;
         5 0 0 0 0;
         0 6 0 0 7;
         0 8 0 0 9;
         0 0 0 0 0;
         0 0 0 0 0; 
         0 0 0 0 0;
         0 0 0 0 0]; % transition matrix
sigma = ["a", "b", "c", "d", "r"]; % alphabet



[Q, q_0, delta, F, sigma] = minimize_DFA(Q, q_0, delta, F, sigma);

delta
