"""
Script for creating System Nets
"""

# Import the DFA data structure from the right file
from models import DFA


def make_valid_region(region,alphabet,delta):
    regions = [region]
    conditions_all_met = False
    while conditions_all_met == False:
        #print("while loop repeat")
        # 
        conditions_all_met = True
        
        for i in range(0,len(regions)):
        
            region = regions[i]
            
            # Rule 1: look for symbols such that: in AND (enter OR exit)
            for e2 in alphabet:
                # Initialise list of states to add
                states_to_add = set()
                
                # Check if e2 is inside the region for any transition
                inside = False # initialise boolean of whether inside
                for transition in delta:
                    if (transition[0] == e2) & (transition[1] in region) & (transition[2] in region):
                        inside = True
                
                # If so,
                if inside == True:
                    #print("symbol:")
                    #print(e2)
                    #print("is inside the region")
                    
                    for transition in delta:
                        # find all states such that there are trasitions from them to the region on e2
                        if (transition[0] == e2) & (transition[2] in region) & (transition[1] not in region):
                            states_to_add = states_to_add | {transition[1]}
                
                        # find all states such that there are trasitions to them from the region on e2
                        if (transition[0] == e2) & (transition[1] in region) & (transition[2] not in region):
                            states_to_add = states_to_add | {transition[2]}
                
                #print("states being added are:")
                #print(states_to_add)
                
                # Check whether there are any states to add, and if so, let the algorithm know that a condition was violated
                if len(states_to_add) > 0:
                    print("Rule 1 violated for event:")
                    print(e2)
                    print("on region:")
                    print(region)
                    conditions_all_met = False
                    region = region | states_to_add
    
    
            # Rule 2
            for e2 in alphabet:
                # Initialise set of states to add
                states_to_add = set()
                
                # Check if e2 enters and exits on any transitions
                enters = False
                exits = False
                for transition in delta:
                    if (transition[0] == e2) & (transition[1] not in region) & (transition[2] in region):
                        enters = True
                    if (transition[0] == e2) & (transition[1] in region) & (transition[2] not in region):
                        exits = True
    
                # If so,
                if (enters == True) & (exits == True):             
                    for transition in delta:
                        # find all states such that there are trasitions from them to the region on e2
                        if (transition[0] == e2) & (transition[2] in region) & (transition[1] not in region):
                            states_to_add = states_to_add | {transition[1]}
                
                        # find all states such that there are trasitions to them from the region on e2
                        if (transition[0] == e2) & (transition[1] in region) & (transition[2] not in region):
                            states_to_add = states_to_add | {transition[2]}
                            
                # Check whether there are any states to add, and if so, let the algorithm know that a condition was violated
                if len(states_to_add) > 0:
                    print("Rule 2 violated for event:")
                    print(e2)
                    print("on region:")
                    print(region)
                    conditions_all_met = False
                    region = region | states_to_add

            
            # Rule 3
            for e2 in alphabet:
                # (Re-)Initialise set of states to add
                states_to_add = set()
                states_to_add_opt2 = set()
                
                # Check if e2 enters and is outside
                enters = False
                outside = False
                for transition in delta:
                    if (transition[0] == e2) & (transition[1] not in region) & (transition[2] in region):
                        enters = True
                    if (transition[0] == e2) & (transition[1] not in region) & (transition[2] not in region):
                        outside = True
                        
                if (enters == True) & (outside == True): # if enter AND out
                    conditions_all_met = False
                    new_region = region
                    print("Rule 3 violated for event:")
                    print(e2)
                    print("on region:")
                    print(region)
                    # Option 1 - change existing region
                    for transition in delta:
                        # find all states such that there are trasitions from them to the region on e2
                        if (transition[0] == e2) & (transition[2] in region) & (transition[1] not in region):
                            states_to_add = states_to_add | {transition[1]}
                        # find all states such that there is a transition to them from a state which is not in the region
                        if (transition[0] == e2) & (transition[1] not in region):
                            states_to_add_opt2 = states_to_add_opt2 | {transition[2]}
                        region = region | states_to_add

                    # Option 2 - add new region to list for this possibility
                    new_region = new_region | states_to_add_opt2
                    regions = regions + [new_region]
                    
            # Rule 4
            for e2 in alphabet:
                # (Re-)Initialise set of states to add
                states_to_add = set()
                states_to_add_opt2 = set()
                
                # Check if e2 enters and is outside
                exits = False
                outside = False
                for transition in delta:
                    if (transition[0] == e2) & (transition[1] in region) & (transition[2] not in region):
                        exits = True
                    if (transition[0] == e2) & (transition[1] not in region) & (transition[2] not in region):
                        outside = True
                        
                if (exits == True) & (outside == True): # if exit AND out
                    conditions_all_met = False
                    new_region = region
                    print("Rule 4 violated for event:")
                    print(e2)
                    print("on region:")
                    print(region)
                    # Option 1 - change existing region
                    for transition in delta:
                        # find all states such that there are trasitions to them from the region on e2
                        if (transition[0] == e2) & (transition[2] not in region) & (transition[1] in region):
                            states_to_add = states_to_add | {transition[2]}
                        # find all states such that there is a transition from them to a state which is not in the region
                        if (transition[0] == e2) & (transition[2] not in region):
                            states_to_add_opt2 = states_to_add_opt2 | {transition[1]}
                        region = region | states_to_add

                    # Option 2 - add new region to list for this possibility
                    new_region = new_region | states_to_add_opt2
                    regions = regions + [new_region]

            # Re-save into list
            regions[i] = region

    return regions



# # Using the DFA in the sample code since it is likely in the right format
#dfa = DFA("Test", {1,2,3}, 1, {1,3}, {("a",1,2), ("b",2,2), ("c",1,3)})

# Using sample code DFA format but DFA from notes about regions
#dfa = DFA("Test", {1,2,3,4}, 1, {4}, {("a",1,2), ("b",1,3), ("b",2,4), ("a",3,4)})

# Simple DFA for testing Rule 1
dfa = DFA("Test", {1,2,3,4}, 1, {2}, {("a",1,4), ("a",2,4), ("b",1,2), ("b",3,2), ("b",1,4)})

# Ultra-simple DFA
#dfa = DFA("Test", {1,2}, 1, {2}, {("a",1,2),("b",2,1),("b",1,2)})

# Extract elments of DFA
Q = dfa.states
delta = dfa.transitions
q0 = dfa.init_state
F = dfa.final_states

# Get alphabet from transitions
alphabet = set() # initialise alphabet as a set in this case
for transition in delta:
    if transition[0] not in alphabet: # the first (0th) element of each transition tuple is the symbol/event being transitioned on
        alphabet = alphabet | {transition[0]}


# Getting (Pre-)Regions of the DFA

region_list = list()

for e in alphabet:
    ### PART 1: For each symbol, find all states such that this event exits
    # Initialise region
    pre_region = set()
    
    # Add states such that there is a transition FROM that state on event e
    for transition in delta:
        if transition[0] == e: # the first element of transition is the symbol
            pre_region = pre_region | {transition[1]} # second element is the state being transitioned FROM

    ### PART 2: Repeat the 4 checks until all conditions are met
    # also turns region into a list of regions
    valid_pre_regions = make_valid_region(pre_region,alphabet,delta)

    # Add region to list of regions
    region_list = region_list + valid_pre_regions
    
    # NOW FIND POST-REGIONS
    # Initialise post-region
    post_region = set()
    
    # Add states such that there is a transition TO that state on event e
    for transition in delta:
        if transition[0] == e: # the first element of transition is the symbol
            post_region = post_region | {transition[2]} # third element is the state being transitioned TO
            
    # Turn the suggested post-region into a valid set of regions
    valid_post_regions = make_valid_region(post_region,alphabet,delta)
    
    # Add to list of regions
    region_list = region_list + valid_post_regions

# Display the list of regions
print(region_list)

# Visualise the DFA (to help us see what we are doing)
dfa.viz()

"""
Sigma = ""
for trace in L:
    for character in trace:
        if character not in Sigma:
            Sigma += character
"""