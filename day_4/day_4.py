# %% SETUP
import os
import os
import pandas as pd
import numpy as np

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

readings = []
with open(file_path) as file:
    for line in file:
        reading = line.split()
        readings.append(list(reading[0]))
# %% PROBLEM 1

def diagonal_search(puzzle: pd.DataFrame) -> int:
    r, c = puzzle.shape
    count = 0
    for i in range(r):
        for j in range(c):
            try:
