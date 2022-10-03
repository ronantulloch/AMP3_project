#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:12:45 2022

@author: william
"""

# IMPORT FILE FOR DFA DATA TYPE AND VISUALISATION
from models import DFA

# Define an Event Log for testing
L = {"abcd","abbbcd","dcba","abc","bcbcbcda"}

# Get alphabet from event log
# Making alphabet a string so that it is ordered
Sigma = ""
for trace in L:
    for character in trace:
        if character not in Sigma:
            Sigma += character
            
# Initialisation:
# Set first state as initial state, representing empty string
q_0 = 1
   
# Initialise list of prefixes (saving as list as order is important)
set_prefixes = ['']
    
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
        current_prefix_set = ""
        for s in Sigma:
            if s in current_prefix:
                current_prefix_set += s
        
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

# Visualise
dfa.viz()
