#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 09:53:55 2022

@author: William Pincombe

Initially this will just be a self-standing script
but if it works, will try to turn into function
"""

# Define Example Event Log / Language
L = {"abc","abd"}

## CONSTRUCTING DFA FROM LANGUAGE (MAIN BIT) ##

# Set first state as initial state, representing empty string
q_0 = 1

# Initialise set of states Q
Q = {q_0}

# Initialise transition function delta as empty set
delta = set()

# Initialise set of final states
final = set()

# Loop across all traces in the event log
for trace in L:
    # Add state for first prefix
    next_index = len(Q) + 1
    Q = Q | {next_index}
    
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
        # add a state for the prefix in Q
        next_index = len(Q) + 1
        Q = Q | {next_index}
        # add a transition to the prefix in delta
        new_transition = (trace[i-1], prev_index, next_index)
        delta = delta | {new_transition}
        # Turn current index into previous index, so that the next prefix can transition from this prefix
        prev_index = next_index

    # Make last prefix final state    
    final = final | {next_index}


# Desired DFA format - note that alphabet is not expressed here
# dfa = DFA("Test", {1,2,3}, 1, {1,3}, {("a",1,2), ("b",2,2), ("c",1,3)})