function [] = DFA_vis(M)
%%Input a DFA in the form of M = {Q, Sigma, delta, q_0, F} and this function will create a
%%visualisation of the graph that relates the states.

%Grab the transition function and states and initialise the graph.
delta = sortrows(M{3}, [2,5]); %Sort rows for conformity.
Q = M{1}; Q = sortrows(Q(2,:));
F = M{5}; F = F(2,:);
q_0 = M{4}; q_0 = q_0(2,1);
final_index = [];
G = digraph;

%Add the nodes to the graph
Q = unique(Q);
for i = 1:length(Q)
	G = addnode(G, Q(i));
	
	%Check if final state.
	if any(Q(i) == F)
		final_index = [final_index, i];
	elseif Q(i) == q_0
		initial_index = i;
	end
end


%Add the transitions to the graph
for i = 1:size(delta,1)
	G = addedge(G, delta(i,2), delta(i,5));
end

%Add the names to the transitions
G.Edges.names = delta(:,3);

%Plot the graph
h = plot(G,'Layout','layered',"EdgeFontAngle", "italic", "Marker", "o");
h.EdgeLabel = G.Edges.names;
highlight(h, final_index, "NodeColor","r"); %Highlight the final states.
highlight(h, initial_index, "NodeColor","g"); %Highlight the initial state.
end