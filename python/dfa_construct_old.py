#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 09:53:55 2022

@author: William Pincombe

Initially this will just be a self-standing script
but if it works, will try to turn into function
"""

# IMPORT FILE FOR DFA DATA TYPE AND VISUALISATION
from models import DFA

# Define an Event Log
L = {"abc","abd","bbc","cdacd","ababc"}

## CONSTRUCT SEQUENCE DFA FROM EVENT LOG ##

# Set first state as initial state, representing empty string
q_0 = 1

# Initialise set of states Q
#Q = {q_0}

# Initialise list of prefixes (Order is Important)
prefixes = ['']

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

# Visualise DFA
dfa.viz()