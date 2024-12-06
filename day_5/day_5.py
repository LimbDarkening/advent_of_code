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


# %% PROBLEM 2
def bad_updates(update: list[int], rules: list[tuple[int, int]]) -> bool:
    for rule in rules:
        if update.index(rule[0]) > update.index(rule[1]):
            return update


wronguns = [
    bad_updates(update, relevant_rules(update, RULES))
    for update in UPDATES
    if bad_updates(update, relevant_rules(update, RULES)) is not None
]


def swap(ls: list, a: int, b: int):
    i = ls.index(a)
    j = ls.index(b)
    ls[i], ls[j] = ls[j], ls[i]
    return ls


def broken_rules(update: list[int], rules: list[tuple[int, int]]):
    broken_rules = []
    for rule in rules:
        if update.index(rule[0]) > update.index(rule[1]):
            broken_rules.append(rule)
    return broken_rules


def fix_update(update: list[int], rules: list[tuple[int, int]]):
    while len(check := broken_rules(update, rules)) > 0:
        update = swap(update, check[0][0], check[0][1])
    return update.pop(len(update) // 2)


print(sum([fix_update(update, relevant_rules(update, RULES)) for update in wronguns]))
# %%
