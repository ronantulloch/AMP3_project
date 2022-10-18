"""
Driver: importing data, constructing DFA and applying markov chain method
"""
# https://compucademy.net/discrete-probability-distributions-with-python/ 

from models import DFA
from dfa_make_irreducible import dfa_make_irreducible
import dfa_construct_all_functions as dfa_construct 

from dfa_to_markov import dfa_to_markov

from pm4py.objects.log.importer.xes import importer as xes_importer

# Import data
variant = xes_importer.Variants.ITERPARSE
parameters = {variant.value.Parameters.TIMESTAMP_SORT: True}
log = xes_importer.apply("data/BPI_Challenge_2013_closed_problems.xes", variant=variant, parameters=parameters)

# Make very simple version of log
#log = log[0:5]


# Convert log to two lists of lists - one for names, the other for timestamps
L = list()
times = list()
for trace in log:
    new_trace = list()
    new_trace_times = list()
    for event in trace:
        new_event = event['concept:name']#+'-'+event['lifecycle:transition']
        new_trace = new_trace + [new_event]
        new_time = event['time:timestamp']
        new_trace_times = new_trace_times + [new_time]
    L = L + [new_trace]
    times = times + [new_trace_times]

# # Alternatively: Get an example DFA and event log to work with 
# #L = [["accepted","queued","completed"],["accepted","queued","rejected"],["accepted","queued","completed"]]

# Construct DFA from data
#dfa = dfa_construct.sequences(L)
dfa = dfa_construct.sequences_windowed(L,1)
dfa.viz()

# Get the Markov Chain transition matrix
(P,f_wait) = dfa_to_markov(dfa,L,times)

##########
"""
# Unpack DFA
Q = dfa.states
delta = dfa.transitions
final_states = dfa.final_states

num_states = len(Q)

# Extract the timestamp data
for trace in log:
    for event in trace:
        print(event['time:timestamp'])


# Initialise list of probability distributions
wait_time = list()

# Get the probability distributions for each possible transition
for i in range(0,num_states):
    for j in range(0,num_states):
        # Get waiting time distribution F_{i,j} for transition from state i to state j

"""

