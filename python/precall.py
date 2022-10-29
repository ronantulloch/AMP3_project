"""
FUNCTION TO CALCULATE PRECISION AND RECALL OF DFA
Input: DFA, event log
Output: (precision, recall)
"""

import dfa_construct_all_functions as dfa_construct
from entropy import entropy

def precall(DFA, event_log):
    # Construct non-windowed sequence DFA from event log for comparison
    # Since this sort of DFA has recall = precision = 1 by definition
    log_DFA = dfa_construct.sequences(event_log)
    
    # Find cross-product of DFA and log
    
    # Calculate entropy of the DFA, and the event log
    ent_DFA = entropy(DFA)
    ent_log = entropy(log_DFA)
    
    # Calculate 
    precision = ent_log/ent_DFA
    recall = ent_log/ent_log
    
    return (precision, recall)