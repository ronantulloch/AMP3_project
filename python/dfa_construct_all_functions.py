"""
All DFA Construction Functions. Accept event logs formatted as lists of lists, as in
[[event1,event2],[event3,event4]]

Catalogue of Functions: what they use (function name)
    1. Sequences (dfa_construct)
    2. Multisets (dfa_construct_multiset)
    3. Sets (dfa_construct_set)
"""

# IMPORT SPECIAL DFA DATA TYPE
from models import DFA

## 1. SEQUENCES ##
def sequences(L):
    # Set first state as initial state, representing empty string
    q_0 = 1
    
    # Initialise set of states Q
    #Q = {q_0}
    
    # Initialise list of prefixes (Order is Important)
    prefixes = [['']]
    
    # Initialise transition function delta as empty set
    delta = set()
    
    # Initialise set of final states
    final = set()
    
    # Loop across all traces in the event log
    for trace in L:
        # FIRST PREFIX:
        # Check whether it is in the list of prefixes already
        already_there = 0
        for j in range(0,len(prefixes)):
            if prefixes[j] == trace[0]:
                next_index = j+1
                already_there = 1
                 
        # If the prefix is not already included in our list, add it
        if already_there == 0:
            prefixes = prefixes + [trace[0]]
            next_index = len(prefixes)
                
        # Add transition from initial state to first prefix, on the first symbol in the trace
        new_transition = (trace[0], q_0, next_index)
        delta = delta | {new_transition}
     
        # Turn current index into previous index, so that the next prefix can transition from this prefix
        prev_index = next_index
     
        # Loop across length of trace - to get all possible prefixes
        for i in range(2,len(trace)+1):
            # Get current prefix 
            current_prefix = trace[0:i]
            #print(current_prefix)
        
            # Check whether it is in the list of prefixes already
            already_there = 0
            for j in range(0,len(prefixes)):
                if prefixes[j] == current_prefix:
                    next_index = j+1
                    already_there = 1
     
            # If the prefix is not already included in our list, add it
            if already_there == 0:
                prefixes = prefixes + [current_prefix]
                next_index = len(prefixes)
        
            # Add a transition from previous prefix to current prefix in delta
            new_transition = (trace[i-1], prev_index, next_index)
            delta = delta | {new_transition}
            # Turn current index into previous index, so that the next prefix can transition from this prefix
            prev_index = next_index
    
        # Make last prefix final state    
        final = final | {next_index}
    
    # Set 
    Q = list(range(1,len(prefixes)+1))
    
    Q = set(Q)
    
    # Save as DFA
    dfa = DFA("Test",Q,q_0,final,delta)
    
    # Return the constructed DFA
    return dfa


## 2. MULTISETS ##
def multisets(L):
    
    # Firstly, we need a function to sort a list into a certain order
    # Modifying a function from this source, which was for strings instead of lists:
    # SOURCE: https://www.geeksforgeeks.org/python-sorting-string-using-order-defined-by-another-string/
    def sortbyPattern(order, list_to_sort):  
        
        # Create a dictionary to store priority of each character
        myDict = { order[i] : i for i in range(len(order))}
      
        # Pass lambda function as key in sort function
        list_to_sort.sort( key = lambda ele : myDict[ele])
      
        return list_to_sort
    
    # Get alphabet from event log
    Sigma = []
    for trace in L:
        for event in trace:
            if event not in Sigma:
                Sigma = Sigma + [event]
    
    # Initialise everything else:
    # Set first state as initial state, representing empty string
    q_0 = 1
       
    # Initialise list of prefixes (saving as list as order is important)
    multiset_prefixes = [['']]
        
    # Initialise sets for transition function and final states
    delta = set()
    final = set()
    
    # Loop over all traces in the event log
    for trace in L:
        # (Re-)Initialise previous state index as 1; since all traces start at the empty initial state
        prev_index = 1
        
        # Loop across length of trace - to get all possible prefixes
        for i in range(1,len(trace)+1):
            # Get current prefix 
            current_prefix = trace[0:i]
            
            # Re-arrange prefix to be in common order (order of the alphabet)
            current_prefix_ordered = sortbyPattern(Sigma,current_prefix)
            
            # Check whether there is already a state corresponding to prefix
            already_there = 0
            for j in range(0,len(multiset_prefixes)):
                if multiset_prefixes[j] == current_prefix_ordered:
                    next_index = j+1
                    already_there = 1
            
            # If not; then add a new state for this prefix
            if already_there == 0:
                multiset_prefixes = multiset_prefixes + [current_prefix_ordered]
                next_index = len(multiset_prefixes)
            
            # Add a transition from previous prefix to current prefix in delta
            new_transition = (trace[i-1], prev_index, next_index)
            delta = delta | {new_transition}
            
            # Turn current index into previous index, so that the next prefix can transition from this prefix
            prev_index = next_index
                    
        # Make last prefix final state    
        final = final | {next_index}
        
    # Set 
    Q = list(range(1,len(multiset_prefixes)+1))
    
    Q = set(Q)
    
    # Save as DFA
    dfa = DFA("Test",Q,q_0,final,delta)
    
    # Return DFA
    return dfa


## 3. SETS ##
def sets(L):
    # Get alphabet from event log
    Sigma = []
    for trace in L:
        for event in trace:
            if event not in Sigma:
                Sigma = Sigma + [event]
                
    # Initialisation:
    # Set first state as initial state, representing empty string
    q_0 = 1
       
    # Initialise list of prefixes (saving as list as order is important)
    set_prefixes = [['']]
        
    # Initialise sets for transition function and final states
    delta = set()
    final = set()
    
    # Loop over all traces in the event log
    for trace in L:
        # (Re-)Initialise previous state index as 1; since all traces start at the empty initial state
        prev_index = 1
        
        # Loop across length of trace - to get all possible prefixes
        for i in range(1,len(trace)+1):
            # Get current prefix 
            current_prefix = trace[0:i]
            
            # Construct set form of prefix by taking each character in the alphabet that is in the prefix
            current_prefix_set = []
            for s in Sigma:
                if s in current_prefix:
                    current_prefix_set = current_prefix_set + [s]
            
            # Check whether there is already a state corresponding to prefix
            already_there = 0
            for j in range(0,len(set_prefixes)):
                if set_prefixes[j] == current_prefix_set:
                    next_index = j+1
                    already_there = 1
            
            # If not; then add a new state for this prefix
            if already_there == 0:
                set_prefixes = set_prefixes + [current_prefix_set]
                next_index = len(set_prefixes)
            
            # Add a transition from previous prefix to current prefix in delta
            new_transition = (trace[i-1], prev_index, next_index)
            delta = delta | {new_transition}
            
            # Turn current index into previous index, so that the next prefix can transition from this prefix
            prev_index = next_index
                    
        # Make last prefix final state    
        final = final | {next_index}
        
    # Set 
    Q = list(range(1,len(set_prefixes)+1))
    
    Q = set(Q)
    
    # Save as DFA
    dfa = DFA("Test",Q,q_0,final,delta)
    
    # Return DFA
    return dfa



## 4. SEQUENCES, WINDOWED ##
def sequences_windowed(L,k):
    # Set first state as initial state, representing empty string
    q_0 = 1
    
    # Initialise list of prefixes (Order is Important)
    prefixes = [['']]
    
    # Initialise transition function delta as empty set
    delta = set()
    
    # Initialise set of final states
    final = set()
    
    # Loop across all traces in the event log
    for trace in L:
        # (Re-)Initialise previous state index as 1; since all traces start at the empty initial state
        prev_index = 1
     
        # Loop across length of trace - to get all possible prefixes
        for i in range(1,len(trace)+1):
            # Get current prefix 
            if i >= k:
                current_prefix = trace[i-k:i]
            else:
                current_prefix = trace[0:i]
            #print(current_prefix)
        
            # Check whether it is in the list of prefixes already
            already_there = 0
            for j in range(0,len(prefixes)):
                if prefixes[j] == current_prefix:
                    next_index = j+1
                    already_there = 1
     
            # If the prefix is not already included in our list, add it
            if already_there == 0:
                prefixes = prefixes + [current_prefix]
                next_index = len(prefixes)
        
            # Add a transition from previous prefix to current prefix in delta
            new_transition = (trace[i-1], prev_index, next_index)
            delta = delta | {new_transition}
            # Turn current index into previous index, so that the next prefix can transition from this prefix
            prev_index = next_index
    
        # Make last prefix final state    
        final = final | {next_index}
    
    # Set 
    Q = list(range(1,len(prefixes)+1))
    
    Q = set(Q)
    
    # Save as DFA
    dfa = DFA("Test",Q,q_0,final,delta)
    
    # Return the constructed DFA
    return dfa



## 5. MULTISETS, WINDOWED ##
def multisets_windowed(L,k):
    
    # Firstly, we need a function to sort a list into a certain order
    # Modifying a function from this source, which was for strings instead of lists:
    # SOURCE: https://www.geeksforgeeks.org/python-sorting-string-using-order-defined-by-another-string/
    def sortbyPattern(order, list_to_sort):  
        
        # Create a dictionary to store priority of each character
        myDict = { order[i] : i for i in range(len(order))}
      
        # Pass lambda function as key in sort function
        list_to_sort.sort( key = lambda ele : myDict[ele])
      
        return list_to_sort
    
    # Get alphabet from event log
    Sigma = []
    for trace in L:
        for event in trace:
            if event not in Sigma:
                Sigma = Sigma + [event]
    
    # Initialise everything else:
    # Set first state as initial state, representing empty string
    q_0 = 1
       
    # Initialise list of prefixes (saving as list as order is important)
    multiset_prefixes = [['']]
        
    # Initialise sets for transition function and final states
    delta = set()
    final = set()
    
    # Loop over all traces in the event log
    for trace in L:
        # (Re-)Initialise previous state index as 1; since all traces start at the empty initial state
        prev_index = 1
        
        # Loop across length of trace - to get all possible prefixes
        for i in range(1,len(trace)+1):
            # Get current prefix 
            if i >= k:
                current_prefix = trace[i-k:i]
            else:
                current_prefix = trace[0:i]
            
            # Re-arrange prefix to be in common order (order of the alphabet)
            current_prefix_ordered = sortbyPattern(Sigma,current_prefix)
            
            # Check whether there is already a state corresponding to prefix
            already_there = 0
            for j in range(0,len(multiset_prefixes)):
                if multiset_prefixes[j] == current_prefix_ordered:
                    next_index = j+1
                    already_there = 1
            
            # If not; then add a new state for this prefix
            if already_there == 0:
                multiset_prefixes = multiset_prefixes + [current_prefix_ordered]
                next_index = len(multiset_prefixes)
            
            # Add a transition from previous prefix to current prefix in delta
            new_transition = (trace[i-1], prev_index, next_index)
            delta = delta | {new_transition}
            
            # Turn current index into previous index, so that the next prefix can transition from this prefix
            prev_index = next_index
                    
        # Make last prefix final state    
        final = final | {next_index}
        
    # Set 
    Q = list(range(1,len(multiset_prefixes)+1))
    
    Q = set(Q)
    
    # Save as DFA
    dfa = DFA("Test",Q,q_0,final,delta)
    
    # Return DFA
    return dfa




## 6. SETS, WINDOWED ##
def sets_windowed(L,k):
    # Get alphabet from event log
    Sigma = []
    for trace in L:
        for event in trace:
            if event not in Sigma:
                Sigma = Sigma + [event]
                
    # Initialisation:
    # Set first state as initial state, representing empty string
    q_0 = 1
       
    # Initialise list of prefixes (saving as list as order is important)
    set_prefixes = [['']]
        
    # Initialise sets for transition function and final states
    delta = set()
    final = set()
    
    # Loop over all traces in the event log
    for trace in L:
        # (Re-)Initialise previous state index as 1; since all traces start at the empty initial state
        prev_index = 1
        
        # Loop across length of trace - to get all possible prefixes
        for i in range(1,len(trace)+1):
            # Get current prefix 
            if i >= k:
                current_prefix = trace[i-k:i]
            else:
                current_prefix = trace[0:i]
            
            # Construct set form of prefix by taking each character in the alphabet that is in the prefix
            current_prefix_set = []
            for s in Sigma:
                if s in current_prefix:
                    current_prefix_set = current_prefix_set + [s]
            
            # Check whether there is already a state corresponding to prefix
            already_there = 0
            for j in range(0,len(set_prefixes)):
                if set_prefixes[j] == current_prefix_set:
                    next_index = j+1
                    already_there = 1
            
            # If not; then add a new state for this prefix
            if already_there == 0:
                set_prefixes = set_prefixes + [current_prefix_set]
                next_index = len(set_prefixes)
            
            # Add a transition from previous prefix to current prefix in delta
            new_transition = (trace[i-1], prev_index, next_index)
            delta = delta | {new_transition}
            
            # Turn current index into previous index, so that the next prefix can transition from this prefix
            prev_index = next_index
                    
        # Make last prefix final state    
        final = final | {next_index}
        
    # Set 
    Q = list(range(1,len(set_prefixes)+1))
    
    Q = set(Q)
    
    # Save as DFA
    dfa = DFA("Test",Q,q_0,final,delta)
    
    # Return DFA
    return dfa