# %% SETUP
import os
import pandas as pd
import numpy as np
import re
import sys
from collections import defaultdict
from typing import Set

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

map = []
with open(file_path) as file:
    for line in file:
        map.append(list(line.strip()))

MAP = pd.DataFrame(map).astype(int)
# %% PROBLEM 1


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def count_valid_trails(
    start: Location, map: pd.DataFrame, visited: Set[Location]
) -> int:

    if map.iloc[start.x, start.y] == 9 and start not in visited:
        visited.add(start)
        return 1

    else:
        neighbours = [
            Location(start.x + 1, start.y),
            Location(start.x - 1, start.y),
            Location(start.x, start.y + 1),
            Location(start.x, start.y - 1),
        ]
        in_map_neighbours = [
            neighbour
            for neighbour in neighbours
            if neighbour.x < map.shape[0]
            and neighbour.x >= 0
            and neighbour.y < map.shape[1]
            and neighbour.y >= 0
        ]
        up_hill_neighbours = [
            neighbour
            for neighbour in in_map_neighbours
            if map.iloc[neighbour.x, neighbour.y] - map.iloc[start.x, start.y] == 1
        ]
        return sum(
            [
                count_valid_trails(neighbour, map, visited)
                for neighbour in up_hill_neighbours
            ]
        )


dummy_map = pd.DataFrame(
    [
        [5, 5, 5, 0, 5, 5, 5],
        [5, 5, 5, 1, 5, 5, 5],
        [5, 5, 5, 2, 5, 5, 5],
        [6, 5, 4, 3, 4, 5, 6],
        [7, 5, 5, 5, 5, 5, 7],
        [8, 5, 5, 5, 5, 5, 8],
        [9, 5, 5, 5, 5, 5, 9],
    ]
)
secound_dummy_map = pd.DataFrame(
    [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2],
    ]
)
third_dummy_map = pd.DataFrame(
    [
        [100, 100, 9, 0, 100, 100, 9],
        [100, 100, 100, 1, 100, 9, 8],
        [100, 100, 100, 2, 100, 100, 7],
        [6, 5, 4, 3, 4, 5, 6],
        [7, 6, 5, 100, 9, 8, 7],
        [8, 7, 6, 100, 100, 100, 100],
        [9, 8, 7, 100, 100, 100, 100],
    ]
)

zeros = [
    count_valid_trails(Location(i, j), MAP, set())
    for i in range(MAP.shape[0])
    for j in range(MAP.shape[1])
    if MAP.iloc[i, j] == 0
]
print(sum(zeros))
# %%
