#! /bin/env python3

import sys
from collections import namedtuple
from typing import List
from functools import reduce

Slope = namedtuple("Slope", "x y")


def get_grid(filepath: str) -> List[str]:
    with open(filepath) as fin:
        return list(x.strip() for x in fin.readlines())


def count_trees_on_path(grid: List[str], slope: Slope) -> int:
    n_trees = 0
    col = 0
    for row in grid[slope.y::slope.y]:
        col = (col + slope.x) % len(row)
        if row[col] == '#':
            n_trees += 1
    return n_trees


def part1(filepath: str) -> int:
    return count_trees_on_path(get_grid(filepath), Slope(3, 1))


def part2(filepath: str) -> int:
    grid = get_grid(filepath)
    slopes = (Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2))
    return reduce(lambda a,b: a * b, map(lambda s: count_trees_on_path(grid, s), slopes))


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))

if __name__ == "__main__":
    main()
