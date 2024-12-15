# %% SETUP
import os
import pandas as pd
import numpy as np
import re
import enum
import matplotlib.pyplot as plt

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

ROBOTS = []
with open(file_path) as file:
    for line in file:
        nums = re.findall(r"-?\d+", line)
        ROBOTS.append([(int(nums[0]), int(nums[1])), (int(nums[2]), int(nums[3]))])

# %% PROBLEM 1
WIDTH = 101
HEIGHT = 103


def quadrant_checker(robot: list[tuple[int, int]]) -> int:
    x, y = robot[0]
    nx, ny = (x + 100 * robot[1][0]) % WIDTH, (y + 100 * robot[1][1]) % HEIGHT

    if nx < 50 and ny < 51:
        return 1
    elif nx < 50 and ny > 51:
        return 2
    elif nx > 50 and ny < 51:
        return 3
    elif nx > 50 and ny > 51:
        return 4
    else:
        return 0


robot_locations = [quadrant_checker(robot) for robot in ROBOTS]
FREQ = pd.Series(robot_locations).value_counts()
print(FREQ[1] * FREQ[2] * FREQ[3] * FREQ[4])

# %% PROBLEM 2


def update_robots(
    robots: list[list[tuple[int, int]]], step: int
) -> list[list[tuple[int, int]]]:
    new_robots = []
    for robot in robots:
        x, y = robot[0]
        nx, ny = (x + step * robot[1][0]) % WIDTH, (y + step * robot[1][1]) % HEIGHT
        new_robots.append([(nx, ny), robot[1]])

    return new_robots


def unique_robots(robots: list[list[tuple[int, int]]]):
    seen = set()
    for robot in robots:
        if robot[0] in seen:
            return False
        seen.add(robot[0])
    return True


i = 0
robots = ROBOTS
while not unique_robots(robots):
    i += 1
    robots = update_robots(robots, 1)


def print_room(robots: list[list[tuple[int, int]]], lable: str):
    coords = pd.DataFrame([robot[0] for robot in robots])
    plt.scatter(coords[0], coords[1])
    plt.savefig(lable)
    plt.cla()


robots = [
    print_room(update_robots(ROBOTS, i), f"Step_{i}.png") for i in range(8167, 8169)
]

# %%
