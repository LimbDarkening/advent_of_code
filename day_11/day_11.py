# %% SETUP
import os
from itertools import chain
import matplotlib.pyplot as plt

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")


with open(file_path) as file:
    for line in file:
        init_stones = [int(stone) for stone in line.split()]

# %%


def apply_rules(stone: int) -> list[int]:
    length = len(str(stone))
    if stone == 0:
        return [1]
    if length % 2 == 0:
        return [int(str(stone)[: length // 2]), int(str(stone)[length // 2 :])]
    else:
        return [stone * 2024]


lenghts = []
stones = init_stones
for step in range(35):
    lenghts.append(len(stones))
    stones = list(chain(*[apply_rules(stone) for stone in stones]))


plt.plot(list(range(1, 36)), lenghts)
plt.show()
# %% PROBLEM 2
from collections import Counter


def apply_rules_counter(stone: int, freq: int) -> Counter:
    length = len(str(stone))
    if stone == 0:
        return Counter({1: freq})
    if length % 2 == 0:
        return Counter({int(str(stone)[: length // 2]): freq}) + Counter(
            {int(str(stone)[length // 2 :]): freq}
        )
    else:
        return Counter({stone * 2024: freq})


def update_counter(stones: Counter) -> Counter:
    new_stones = Counter()
    for stone in stones.keys():
        new_stones.update(apply_rules_counter(stone, stones[stone]))
    return new_stones


stone_counter = Counter(init_stones)
for i in range(75):
    stone_counter = update_counter(stone_counter)

print(sum(list(stone_counter.values())))
# %%
