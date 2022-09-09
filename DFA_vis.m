function [] = DFA_vis(M)
%%Input a DFA in the form of M = {Q, Sigma, delta, q_0, F} and this function will create a
%%visualisation of the graph that relates the states.

%Grab the transition function and states and initialise the graph.
delta = M{3};
Q = M{1}; Q = Q(2,:);
G = digraph;

%Add the nodes to the graph
for i = 1:length(Q)
	G = addnode(G, Q(i));
end


%Add the transitions to the graph
for i = 1:size(delta,1)
	G = addedge(G, delta(i,2), delta(i,5));
end


%Plot the graph
plot(G);
end