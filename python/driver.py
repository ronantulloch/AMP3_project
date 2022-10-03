#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:43:30 2022

@author: william
"""

# Import algorithms
from dfa_construct import dfa_construct
from dfa_construct_generalised import dfa_construct_generalised
#from dfa_construct_generalised_windowed import dfa_construct_generalised_windowed

from transition_matrix_state_by_state import dfa_transition_matrix
from dfa_make_irreducible import dfa_make_irreducible
from entropy import entropy

# Define an Event Log
#L = {"abc","abd","bbc","cdacd","ababc"}

# Run the DFA Construct algorithm
#dfa = dfa_construct(L)

# A more general case
L = [["accepted","queued","completed"],["accepted","queued","rejected"]]
dfa = dfa_construct_generalised(L)

# Use function to find with window size of 2
#L = [["a","b","c"],["a","b","d","b","c"]]
#dfa = dfa_construct_generalised_windowed(L,2)

# Make the DFA irreducible
#dfa = dfa_make_irreducible(dfa)

# Find transition matrix
#transition_matrix = dfa_transition_matrix(dfa)

# Print the transition matrix
#print(transition_matrix)

# Visualise DFA
dfa.viz()

# Calculate entropy of dfa
entropy1 = entropy(dfa)
print(entropy1)