#! /bin/env python3

import sys
from typing import Tuple, List
from math import ceil, floor

def get_seats(filepath: str) -> List[str]:
    with open(filepath) as fin:
        for line in fin:
            yield line


def calc_row_col(seat: str) -> Tuple[int, int]:
    row_range = [0, 127]
    col_range = [0, 7]

    for r in seat[:7]:
        if r == 'F':
            row_range[1] = floor((row_range[1] + row_range[0]) / 2)
        else:
            row_range[0] = ceil((row_range[0] + row_range[1]) / 2)

    for c in seat[7:]:
        if c == 'L':
            col_range[1] = floor((col_range[1] + col_range[0]) / 2)
        else:
            col_range[0] = ceil((col_range[0] + col_range[1]) / 2)

    return row_range[0], col_range[1]

def get_all_ids(filepath: str) -> List[int]:
    return map(lambda rc: rc[0] * 8 + rc[1], map(calc_row_col, get_seats(filepath)))


def part1(filepath: str) -> int:
    return max(get_all_ids(filepath))


def part2(filepath: str) -> int:
    sorted_ids = sorted(get_all_ids(filepath))
    for i in range(0, len(sorted_ids) - 1):
        if sorted_ids[i] != sorted_ids[i+1] - 1:
            return sorted_ids[i] + 1


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))


if __name__ == "__main__":
    main()
