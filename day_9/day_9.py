# %% SETUP
import os
import pandas as pd
import numpy as np
import re
import sys
from collections import defaultdict

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

disk = []
with open(file_path) as file:
    for line in file:
        disk.append(line)

# %% PROBLEM 1


def uncompress(disk: str) -> list[int]:
    uncompressed_disk = []
    for i, bit in enumerate(disk):
        if i % 2 == 0:
            uncompressed_disk += [int(i / 2) for _ in range(int(bit))]
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


print(check_sum(uncompress(disk[0])))

# %% PROBLEM 2


def file_decompress(disk: str) -> list[list[str]]:
    uncompressed_disk = []
    for i, bit in enumerate(disk):
        if bit == "0":
            continue
        if i % 2 == 0:
            uncompressed_disk.append([int(i / 2) for _ in range(int(bit))])
        else:
            uncompressed_disk.append(list("." * int(bit)))
    return uncompressed_disk


def file_orderer(uncompressed_disk: list[list[str]]) -> list[tuple[int, int]]:

    # build space dictionary
    space = defaultdict(list)
    for i, row in enumerate(uncompressed_disk):
        if row[0] == ".":
            space[len(row)].append(i)
    max_space = max(space.keys())

    file_order = []
    for i, row in enumerate(reversed(uncompressed_disk)):
        if row[0] != ".":
            possible_sizes = range(len(row), max_space + 1)
            set_ = False
            for size in possible_sizes:
                if len(space[size]) != 0:
                    file_order.append((row, space[size].pop(0)))
                    set_ = True
                    break
            if not set_:
                file_order.append((row, len(uncompressed_disk) - i))

    return file_order


def file_sum(file_order: list[tuple[int, int]]) -> int:
    s = 0
    for file in file_order:
        s += sum(
            [
                i * j
                for i, j in zip(
                    file[0], list(range(file[1], file[1] + len(file[0]) + 1))
                )
            ]
        )
    return s


print(file_sum(file_orderer(file_decompress("2333133121414131402"))))

# %%
