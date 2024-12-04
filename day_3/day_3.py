# %% SETUP
import os
import os
import pandas as pd
import numpy as np
import re

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

bad_data = []
with open(file_path) as file:
    for line in file:
        bad_data.append(line)

# %% PROBLEM 1


def calc(line: str) -> int:
    numbers = re.findall(r"\d+", line)
    return int(numbers[0]) * int(numbers[1])


def find_valid_codes(bad_data: str) -> str:
    valid_codes = re.findall(r"mul\(\d{1,3},\d{1,3}\)", bad_data)
    return valid_codes


print(
    sum(
        sum([calc(line) for line in find_valid_codes(bad_data_str)])
        for bad_data_str in bad_data
    )
)

# %%
