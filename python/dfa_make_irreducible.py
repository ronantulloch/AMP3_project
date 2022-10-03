"""
Function to make a DFA irreducible
by adding transitions from the final states to the initial state, on a 
"""

from models import DFA

def dfa_make_irreducible(dfa):
    # "unpack" the DFA
    delta = dfa.transitions
    F = dfa.final_states
    q0 = dfa.init_state
    
    # New transition event
    event = "SPECIAL_IRREDUCIBILITY_EVENT"
    
    # Check that event is not in the alphabet
    
    # Firstly, find the alphabet from the transitions
    alphabet = []
    for d in delta:
        if d[0] not in alphabet:
            alphabet = alphabet + [d[0]]
    
    # If the special event is in the alphabet, add dashes until it is not
    while event in alphabet:
        event += "-"
    
    # For each final state, add a transition on the special
    for f in F:
        new_transition = (event,f,q0)
        delta = delta | {new_transition}
        
    # Re-pack the transitions of the DFA
    dfa.transitions = delta
    
    # Return the modified DFA
    return dfa