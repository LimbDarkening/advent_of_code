# %% SETUP
import os
import pandas as pd
import numpy as np
import re

current_dir = os.path.dirname(__file__)
rules_path = os.path.join(current_dir, "rules.txt")
updates_path = os.path.join(current_dir, "updates.txt")

RULES = []
with open(rules_path) as file:
    for line in file:
        reading = line.split("|")
        RULES.append((int(reading[0].strip()), int(reading[1].strip())))

UPDATES = []
with open(updates_path) as file:
    for line in file:
        reading = line.split(",")
        UPDATES.append([int(i) for i in reading])

# %% PROBLEM 1


def relevant_rules(
    update: list[int], rules: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    return [rule for rule in rules if rule[0] in update and rule[1] in update]


def validate(update: list[int], rules: list[tuple[int, int]]) -> bool:
    for rule in rules:
        if update.index(rule[0]) > update.index(rule[1]):
            return 0
    return update.pop(len(update) // 2)


print(sum([validate(update, relevant_rules(update, RULES)) for update in UPDATES]))
