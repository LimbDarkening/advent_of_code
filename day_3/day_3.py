# %% SETUP
import os
import os
import pandas as pd
import numpy as np
import re

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

bad_data = ""
with open(file_path) as file:
    for line in file:
        bad_data += line
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

# %% PROBLEM 2


def find_valid_and_conditionals(bad_data: str) -> str:
    valid_codes = re.findall(r"(do\(\)|mul\(\d{1,3},\d{1,3}\)|don't\(\))", bad_data)
    return valid_codes


def conditional_calc(bad_data: str) -> int:
    sum = 0
    mul_switch = 1
    ops = find_valid_and_conditionals(bad_data)
    for op in ops:
        if op == "do()":
            mul_switch = 1
        elif op == "don't()":
            mul_switch = 0
        else:
            sum += mul_switch * calc(op)
    return sum


print(conditional_calc(bad_data))

# %%
