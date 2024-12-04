# Problem 1
# %%
import os
import os
import pandas as pd
import numpy as np

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

readings = []
with open(file_path) as file:
    for line in file:
        reading = line.split()
        readings.append(reading)


def valid(reading: list[int]) -> bool:
    init_monitonic = 0
    for i, r in enumerate(reading[:-1]):
        dif = int(reading[i + 1]) - int(r)
        if dif == 0 or abs(dif) > 3:
            return False
        if init_monitonic == 0:
            init_monitonic = 1 if dif > 0 else -1
        else:
            implied_flag = 1 if dif > 0 else -1
            if implied_flag != init_monitonic:
                return False
    return True


def valid_pd(reading: list[int]) -> bool:
    array = pd.Series([int(i) for i in reading])
    diffs = array.diff()[1:]
    monitonic = np.all(diffs > 0) or np.all(diffs < 0)
    small = np.all(diffs.abs() <= 3) and np.all(diffs.abs() >= 1)
    return monitonic and small


import time

t1 = time.time()
print(sum([valid(r) for r in readings]))
print(f"Time: {time.time() - t1}")

t2 = time.time()
print(sum([valid_pd(r) for r in readings]))
print(f"Time: {time.time() - t2}")


# %%
