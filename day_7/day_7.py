# %% SETUP
import os
import pandas as pd
import numpy as np
import re
import enum
from typing import Tuple

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

readings = []
with open(file_path) as file:
    for line in file:
        target, numbers = line.split(":")
        readings.append((int(target), [int(i) for i in numbers.split()]))


# %% Problem 1

def can_make_result(numbers: list[int], target: int) -> bool:
    def backtrack(index: int, current_result: int):
        if index == len(numbers):
            return current_result == target
        next_num = numbers[index]
        return backtrack(index + 1, current_result + next_num) or backtrack(
            index + 1, current_result * next_num
        )

    return backtrack(1, numbers[0])


correct = [target for target, numbers in readings if can_make_result(numbers, target)]
print(sum(correct))

# %%
