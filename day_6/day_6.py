# %% SETUP
import os
import pandas as pd
import numpy as np
import re
import enum

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

readings = []
with open(file_path) as file:
    for line in file:
        reading = line.split()
        readings.append(list(reading[0]))


# %% PROBLEM 1
class Direction(enum.Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "V"
    LEFT = "<"


class Guard:
    def __init__(self, i: int, j: int, d: Direction):
        self.i = i
        self.j = j
        self.d = d

    def update_state(self) -> None:
        options = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        self.d = (
            options[options.index(self.d) + 1]
            if options.index(self.d) + 1 < len(options)
            else options[0]
        )


def get_ray(guard: Guard, room: pd.DataFrame) -> pd.Series:
    match guard.d:
        case Direction.UP:
            return room.iloc[0 : guard.i, guard.j]
        case Direction.RIGHT:
            return room.iloc[guard.i - 1, guard.j :]
        case Direction.DOWN:
            return room.iloc[guard.i - 1 :, guard.j]
        case Direction.LEFT:
            return room.iloc[guard.i + 1, guard.j]
