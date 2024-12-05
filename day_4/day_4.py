# %% SETUP
import os
import os
import pandas as pd
import numpy as np
import re

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

readings = []
with open(file_path) as file:
    for line in file:
        reading = line.split()
        readings.append(list(reading[0]))
# %% PROBLEM 1

import numpy as np

def get_diagonals(matrix: pd.DataFrame):
    diags = []

    for start_col in range(matrix.shape[1]):
        diags.append(np.diagonal(matrix, offset=start_col))
    for start_row in range(1, matrix.shape[0]):
        diags.append(np.diagonal(matrix, offset=-start_row))

    return diags

def get_rows_and_cols(matrix: pd.DataFrame):
    paths = []
    for i in range(matrix.shape[1]):
        paths.append(matrix.iloc[:, i])
    for i in range(matrix.shape[0]):
        paths.append(matrix.iloc[i, :])

    return paths

def find_xmas(path: list[str]) -> int:
    return len(re.findall(r"XMAS", "".join(path))) + len(
        re.findall(r"SAMX", "".join(path))
    )

r_diags = get_diagonals(pd.DataFrame(readings))
l_diags = get_diagonals(np.fliplr(pd.DataFrame(readings)))
rows_and_cols = get_rows_and_cols(pd.DataFrame(readings))
print(sum(find_xmas(path) for path in l_diags + r_diags + rows_and_cols))

# %%
