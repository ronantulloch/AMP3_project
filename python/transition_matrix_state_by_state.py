"""
Function inputing a DFA and outputing a square transition matrix with dimensions
given by the number of states and numbers indicating the number of possible transitions
from the row state to the column state
"""

# Import DFA data structure
from models import DFA

# Import numpy for matrices
import numpy as np

def dfa_transition_matrix(dfa):
    # Extract states and transitions
    Q = dfa.states
    delta = dfa.transitions
    
    # Get number of states
    num_states = len(Q)
    
    # Initialise transition matrix as array of zeros
    transition = np.zeros((num_states, num_states))
    
    # For each transition from state i to state j, add 1 to transitions[i][j]
    for i in range(0,num_states):
        for j in range(0,num_states):
            for d in delta:
                if (d[1] == i+1) & (d[2] == j+1):
                    transition[i][j] = transition[i][j] + 1
    
    # Return the transition matrix
    return transition