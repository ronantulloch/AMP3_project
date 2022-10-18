"""
Converting DFA with Event Log to Markov Chain

Takes a valid DFA and an event log
Outputs tuple: (Markov Chain transition matrix, list of waiting time distributions)
"""

from models import DFA
#from dfa_make_irreducible import dfa_make_irreducible
#import dfa_construct_all_functions as dfa_construct 
import numpy as np # for matrix commands

def dfa_to_markov(dfa,L,times):

    # Extract states and transition relation from DFA
    Q = dfa.states
    delta = dfa.transitions
    init_state = dfa.init_state
    final_states = dfa.final_states
    
    # Get number of states
    num_states = len(Q)
    
    # Initialise transition matrix P as array of zeros
    # All states in model (including initial state); and added final state
    P = np.zeros((num_states+1, num_states+1))
    
    # Initialise counters of transitions between each combination of states
    transition_counters = np.zeros((num_states+1, num_states+1))
    
    # Initialise counters of total number of transitions from each state
    total_counters = np.zeros((num_states+1))
    
    # Initialise list of lists of times
    f_wait = list()
    for i in range(0,num_states):
        for j in range(0,num_states):
            # Initialise a list for each possible transition
            name = 'f_{'+str(i+1)+','+str(j+1)+'}'
            new_list = list()
            f_wait = f_wait+[(name,new_list)]
            
    
    # For each trace in the event log
    for j in range(0,len(L)):
        # STRATEGY: At each step in the trace, find the transition being performed, then:
        #   - add to the counters for that transition
        #   - get the time taken for the transition, and add this to the appropriate list of times
        
        # Extract the event names (trace) and timestamps
        trace = L[j]
        trace_times = times[j]
        
        # CHECK that the lists of names and timestamps are the same length. 
        if len(trace) != len(trace_times):
            raise ValueError("MAJOR ERROR: List of timestamps not same length as list of names for a trace")
        
        # All traces start at the initial state
        current_state = 1
        
        # Go through all the positions in the trace
        for i in range(0,len(trace)):
            
            # Check if we are in a final state
            #if current_state in final_states:            
                # Go to the next trace
                #break
            
            # Get the next event in the transition
            next_event = trace[i]
            
            #print("for the prefix:")
            #print(trace[0:i])
            
            # Find next state, by: searching all transitions to find the one which leaves the current state with the desired event
            for d in delta:
                if (d[1] == current_state) & (d[0] == next_event):
                    
                    # Get next state
                    next_state = d[2]
                    
                    # We are done
                    break
            
            # Add to the counter of total transitions 
            total_counters[current_state - 1] = total_counters[current_state - 1] + 1
        
            # Add to the counter for transitions between these states
            transition_counters[current_state - 1][next_state - 1] = transition_counters[current_state - 1][next_state - 1] + 1
            
            # Get the time taken by the transition
            # - only works if we are past the first spot in the trace, because it doesn't have a previous timestamp to compare to
            if i > 0:
                # Take difference in timestamps
                time_taken = trace_times[i] - trace_times[i-1]
                
                # Conver the time into seconds
                time_taken = time_taken.total_seconds()
                
                # Add this time to the appropriate list
                f_wait[num_states*(current_state - 1) + (next_state - 1)][1].append(time_taken) # [1] to get the list rather than the name
            
            # Move on to the next state
            current_state = next_state
            
        # Add transition from end of trace to the new final state
        transition_counters[current_state - 1][num_states] = transition_counters[current_state - 1][num_states] + 1
        # And so also increment the counter for the last state
        total_counters[current_state - 1] = total_counters[current_state - 1] + 1

    # Add transition back to initial state in the counters
    total_counters[num_states] = 1
    transition_counters[num_states][0] = 1
    
    # Get transition probabilities from counters
    for i in range(0,num_states+1):
        for j in range(0,num_states+1):
            P[i][j] = transition_counters[i][j]/total_counters[i]
    
    
    #print(transition_counters)
    #print("")
    #print(total_counters)
    #print("")
    #print(P)
    
    return (P,f_wait)