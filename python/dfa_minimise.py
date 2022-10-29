"""
FUNCTION FOR MINIMISING DFA
"""

from models import DFA

def dfa_minimise(dfa):
    # Extract elements of DFA
    name = dfa.name
    states = dfa.states
    init_state = dfa.init_state
    transitions = dfa.transitions
    final_states = dfa.final_states
    
    ## PART 1 : Totally-define the DFA ##
    
    # Add dead state
    dead_state_ID = len(states) + 1
    states = states | {dead_state_ID}
    
    # Get alphabet from transitions
    alphabet = set() # initialise alphabet as a set in this case
    for transition in transitions:
        if transition[0] not in alphabet: # the first (0th) element of each transition tuple is the symbol/event being transitioned on
            alphabet = alphabet | {transition[0]}

    
    # Add transitions to dead state
    for state in states:
        for event in alphabet:
            # Check whether there is a transition
            is_transition = False
            for transition in transitions:
                if ((transition[0] == event) & (transition[1] == state)):
                    is_transition = True
            
            # If there is no transition, add a transition to the dead state
            if is_transition == False:
                new_transition = (event, state, dead_state_ID)
                transitions = transitions | {new_transition}

    ## PART 2 : Merge Irreducible States ##
    
    # Initialise two groups, and group of groups
    group_1 = states - final_states # all non-final states
    group_2 = final_states # all final states
    groups = [group_1, group_2]
    
    # Now split groups based on transition behaviour
    done = False # initialising indicator of algorithm completeness
    while done == False:
        print("Iteration")
        print("Groups:")
        print(groups)
        print("")
        done = True # if no changes are made, this will remain True at the end of an interation, and so we will know the algorithm is complete
        for group in groups:
            # Take a sample state in the group to compare to
            sample_in_group = next(iter(group))
            for event in alphabet:
                # Initialise set of states to split off
                to_split = set()
                
                # Find the sample state's destination on this event
                for transition in transitions:
                    if (transition[0] == event) & (transition[1] == sample_in_group):
                        base_destination = transition[2]
                        break
                print("")
                print("For group: ",group)
                print("On Symbol: ",event)
                print("Comparison destination is: ",base_destination)
                # For each state in the group
                for state in group:
                    # Find destination
                    for transition in transitions:
                        if (transition[0] == event) & (transition[1] == state):
                            state_destination = transition[2]
                    # If destination not same as base destination, then indicate state should be split off and that the algorithm is not done
                    if state_destination != base_destination:
                        print("destination: ",state_destination," of state: ",state," does not match")
                        to_split = to_split | {state}
                        done = False
                
                # Add new group to list of groups, if it exists
                if len(to_split) > 0:
                    # Remove elements in new group from old group 
                    for element in to_split:
                        group.remove(element)
                    # Add new group
                    groups = groups + [to_split]
                    
        # de-duplicate groups
        #done2 = False
        #while done2 == False:
        #    done2 = True
        #    for i in range(0,len(groups)):
        #        if (groups[i] in groups[0:i]) | (groups[i] in groups[i+1:len(groups)]):
        #            del groups[i]
        #            done2 = False
        #            break
    
    # Set minimised states as indices of groups
    min_states = set(range(1,len(groups)+1))
    
    # Initialise minimised transitions
    min_transitions = set()
    
    # Construct minimised transitions based on group behaviour
    for transition in transitions:
        for i in range(0,len(groups)):
            # Find origin group
            if transition[1] in groups[i]:
                orig = i+1
            # Find destination group
            if transition[2] in groups[i]:
                dest = i+1
        # Add transition between these groups, if it isn't already in set
        min_transitions = min_transitions | {(transition[0],orig,dest)}

    # Find group containing initial state, set as minimised initial state
    for i in range(0,len(groups)):
        if init_state in groups[i]:
            min_init_state = i+1
    
    # Find which groups contain final states, add these groups to minimised final states
    min_final_states = set()
    for i in range(0,len(groups)):
        for final_state in final_states:
            if final_state in groups[i]:
                min_final_states = min_final_states | {i+1}

    min_DFA = DFA(name, min_states, min_init_state, min_final_states, min_transitions)
    return min_DFA