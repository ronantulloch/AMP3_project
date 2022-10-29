# DRIVER SCRIPT FOR TESTING DFA MINIMISATION ALGORITHM

from models import DFA
import dfa_construct_all_functions as dfa_construct
from dfa_minimise import dfa_minimise

log = [["a","a","b"],["a","b"],["b","b"]]

model = dfa_construct.sequences(log)
model.viz()

model_min = dfa_minimise(model)
model_min.viz()