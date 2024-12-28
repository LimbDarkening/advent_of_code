# %% SETUP
import os
import pandas as pd
import numpy as np
import re
import enum
import matplotlib.pyplot as plt
from typing import Set

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

blocks = []
with open(file_path) as file:
    for line in file:
        x, y = line.split(",")
        blocks.append((int(x), int(y)))

# %% PROBLEM 1

from heapq import heapify, heappop, heappush


def generate_valid_nodes(bound: int, blocks: Set[tuple[int, int]]):
    starting_coords = set()
    for x in range(bound):
        for y in range(bound):
            starting_coords.add((x, y))
    return starting_coords.difference(blocks)


def create_adjacency_list(
    nodes: Set[tuple[int, int]]
) -> dict[tuple[int, int], dict[tuple[int, int], int]]:
    adjacency_list = {}
    for node in nodes:
        adjacency_list[node] = {}
        for adj in nodes:
            if adj[0] == node[0] + 1 and adj[1] == node[1]:
                adjacency_list[node][adj] = 1
            elif adj[0] == node[0] - 1 and adj[1] == node[1]:
                adjacency_list[node][adj] = 1
            elif adj[0] == node[0] and adj[1] == node[1] + 1:
                adjacency_list[node][adj] = 1
            elif adj[0] == node[0] and adj[1] == node[1] - 1:
                adjacency_list[node][adj] = 1
    return adjacency_list


def dijkstra(
    adjacency_list: dict[tuple[int, int], dict[tuple[int, int], int]]
) -> dict[tuple[int, int], float]:
    init_distance = {node: float("inf") for node in adjacency_list}
    init_distance[(0, 0)] = 0
    pq = [(0, (0, 0))]
    heapify(pq)
    visited = set()
    while pq:
        distance, node = heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        for neighbour, weight in adjacency_list[node].items():
            new_distance = distance + weight
            if new_distance < init_distance[neighbour]:
                init_distance[neighbour] = new_distance
                heappush(pq, (new_distance, neighbour))
    return init_distance


adjacency_list = create_adjacency_list(generate_valid_nodes(71, set(blocks[:1024])))
paths = dijkstra(adjacency_list)


# %% PROBLEM 2


def critical_block(blocks: list[tuple[int, int]]):
    i = 2950
    while dijkstra(create_adjacency_list(generate_valid_nodes(71, set(blocks[:i]))))[
        (70, 70)
    ] < float("inf"):
        print(i)
        i += 1
    return i


idx = critical_block(blocks)
print(blocks[idx - 1])

# %%
