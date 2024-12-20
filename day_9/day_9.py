# %% SETUP
import os
import pandas as pd
import numpy as np
import re
import sys

sys.set_int_max_str_digits(0)
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

disk = []
with open(file_path) as file:
    for line in file:
        disk.append(line)

# %% PROBLEM 1


def chunk_disk(disk: str, chunk_size: int) -> list[str]:
    return [disk[i : i + chunk_size] for i in range(0, len(disk), chunk_size)]


def uncompress(disk: str) -> list[str]:
    uncompressed_disk = []
    for i, bit in enumerate(disk):
        if i % 2 == 0:
            uncompressed_disk += list(str(int(i / 2)) * int(bit))
        else:
            uncompressed_disk += list("." * int(bit))
    return uncompressed_disk


def check_sum(uncompressed_disk: list[str]) -> int:
    digit_count = len([i for i in uncompressed_disk if i != "."])
    left_sums = [
        i * int(bit)
        for i, bit in enumerate(uncompressed_disk[:digit_count])
        if bit != "."
    ]
    dot_indexes_left = [
        i for i, bit in enumerate(uncompressed_disk[:digit_count]) if bit == "."
    ]
    digits_right = [int(bit) for bit in uncompressed_disk[digit_count:] if bit != "."]
    right_sums = [i * int(bit) for i, bit in zip(dot_indexes_left, digits_right[::-1])]
    return sum(left_sums) + sum(right_sums)


# print(check_sum("".join([uncompress(chunk) for chunk in chunk_disk(disk[0], 1000)])))
print(check_sum(uncompress(disk[0])))

# %%
