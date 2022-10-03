#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:01:28 2022

@author: William Pincombe
"""

# IMPORT FILE FOR DFA DATA TYPE AND VISUALISATION
from models import DFA

## A FUNCTION TO SORT A STRING INTO CERTAIN ORDER ##
# SOURCE: https://www.geeksforgeeks.org/python-sorting-string-using-order-defined-by-another-string/
def sortbyPattern(pat, str):  

    priority = list(pat)  

    # Create a dictionary to store priority of each character
    myDict = { priority[i] : i for i in range(len(priority))}
  
    str = list(str)
  
    # Pass lambda function as key in sort function
    str.sort( key = lambda ele : myDict[ele])
  
    new_str = ''.join(str)
    return new_str


# Define an Event Log for testing
L = {"abc","abcd","dcba"}

# Get alphabet from event log
# Making alphabet a string so that it is ordered
Sigma = ""
for trace in L:
    for character in trace:
        if character not in Sigma:
            Sigma += character
            
# Initialise everything else:
# Set first state as initial state, representing empty string
q_0 = 1
   
# Initialise list of prefixes (saving as list as order is important)
multiset_prefixes = ['']
    
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

# Visualise
dfa.viz()
