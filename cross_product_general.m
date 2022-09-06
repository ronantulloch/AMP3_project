% using good definition for cross-product: http://thebeardsage.com/constructing-the-cross-product-of-2-dfas/
% ASSUME: DFAs only have one transition from each state on each symbol
function [M_cp] = cross_product_general(M1,M2)
% Accepts DFAs of format: M = {Q, Sigma, delta, q_0, F}, where
%   - Q is just a list of numbers for the number of states
%   - Sigma is a string array consisting of the list of symbols in the
%   alphabet
%   - delta is a string array with 3 columns, where:
%       - column 1: index of state being transitioned from in Q
%       - column 2: symbol being transitioned on
%       - column 3: index of state being transitioned to in Q
%   - q_0 is the index of the initial state in Q
%   - F is a list of the indices of the final states in Q

% Get alphabet
Sigma = M1{2}; % should be the same?!?!!

% Get lists of states
Q1 = M1{1};
Q2 = M2{1};

% Increment Q2
% Q2 = Q2 + length(Q1);

% Get transitions
delta1 = M1{3};
delta2 = M2{3};

% Get final states
F1 = M1{5};
F2 = M2{5};

% Initialise list of combined states
Q_cp = [];

% Initialise list of combined final states
F_cp = [];

% state_num = 0;

% Add all possible combinations to list of combined states
for i = 1:length(Q1)
    for j = 1:length(Q2)
        new = string(i)+"x"+string(j);
%         state_num = state_num + 1;
        Q_cp = [Q_cp,new];
        if any(ismember(F1,i))
            if any(ismember(F2,j))
                F_cp = [F_cp, new];
            end
        end
    end
end

% Add state numbers to Q
Q_cp = [1:length(Q_cp);Q_cp];

% Set initial state to be the state combining initial states
q_0_cp = string(M1{4})+"x"+string(M2{4});

q_0_cp = Q_cp(1,find(ismember(Q_cp(2,:),to)));

% Initialise new transition function for cross product
delta_cp = strings(1,3);

% 
for sigma = 1:length(Sigma)
    for i = 1:length(Q1)
        for j = 1:length(Q2)
            % where delta1 goes for i,sigma
            dest1 = delta1(find(ismember(delta1(:,1:2),[string(i),Sigma(sigma)],'rows')),3);
            % where delta2 goes for j,sigma
            dest2 = delta2(find(ismember(delta2(:,1:2),[string(j),Sigma(sigma)],'rows')),3);
            
            % So long as both exist, send state corresponding to i*j to dest1*dest2
            if ~(isempty(dest1) || isempty(dest2))
                from = string(i)+"x"+string(j);
                to = string(dest1)+"x"+string(dest2);
                
                % Find indices of "from" and "to" in Q_cp
                from_num = Q_cp(1,find(ismember(Q_cp(2,:),from)));
                to_num = Q_cp(1,find(ismember(Q_cp(2,:),to)));
                
                new = [from_num, Sigma(sigma), to_num];
                delta_cp = [delta_cp;new];
            end
        end
    end
end
delta_cp = delta_cp(2:end,:);

% Somewhat optional: remove names of states in cross-product DFA
Q_cp = Q_cp(1,:);

M_cp = {Q_cp, Sigma, delta_cp, q_0_cp, F_cp};
end
