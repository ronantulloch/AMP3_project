"""
Function for calculating the entropy of a DFA
"""

from models import DFA
from dfa_make_irreducible import dfa_make_irreducible
from transition_matrix_state_by_state import dfa_transition_matrix 

import numpy as np

def entropy(dfa):
    # Call function to make DFA irreducible
    dfa = dfa_make_irreducible(dfa)
    
    # Call transition matrix function
    transitions = dfa_transition_matrix(dfa)
    
    # Find eigenvalues of transition matrix
    eigenvalues = np.linalg.eig(transitions)[0]
    eigenvalues = eigenvalues.real
    entropy = np.log2(max(eigenvalues))
    
    return entropy