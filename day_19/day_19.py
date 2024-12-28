# %% SETUP
import os
import pandas as pd
import numpy as np
import re
import enum
import matplotlib.pyplot as plt

current_dir = os.path.dirname(__file__)
file_path_towles = os.path.join(current_dir, "input_1.txt")
file_path_patterns= os.path.join(current_dir, "input_2.txt")


with open(file_path_towles) as file:
    for line in file:
        TOWELS = line.split(",")

PATTERNS = []
with open(file_path_patterns) as file:
    for line in file:
        PATTERNS.append(line)