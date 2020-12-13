#! /bin/env python3

import sys
from typing import List, Callable
from enum import Enum

class Tile(Enum):
    EMPTY, FLOOR, OCCUPIED = 'L', '.', '#'


def get_floor_plan(filepath: str) -> List[List[Tile]]:
    tile_table = {'L': Tile.EMPTY, '.': Tile.FLOOR, '#': Tile.OCCUPIED}
    to_tile = lambda t: tile_table[t]
    return list(map(lambda l: [to_tile(t) for t in l], filter(lambda l: l != '', open(filepath).read().split('\n'))))


def simulate(floor_plan: List[List[Tile]], should_update: Callable[[List[List[Tile]], int, int], bool]) -> int:
    def update(r, c):
        floor_plan[r][c] = Tile.OCCUPIED if floor_plan[r][c] == Tile.EMPTY else Tile.EMPTY

    seats = []
    for r, row in enumerate(floor_plan):
        for c, tile in enumerate(row):
            if tile != Tile.FLOOR:
                seats.append((r, c))

    while True:
        to_update = []
        for r, c in seats:
            if should_update(floor_plan, r, c):
                to_update.append((r, c))

        if len(to_update) == 0:
            break

        for r, c in to_update:
            update(r, c)

    return sum(list(map(lambda rc: 1 if floor_plan[rc[0]][rc[1]] == Tile.OCCUPIED else 0, seats)))


def part1(filepath: str) -> int:
    floor_plan = get_floor_plan(filepath)

    def should_update(floor_plan, r, c):
        def get_n_occupied_neighbors(r, c):
            n_occupied_neighbors = 0
            for row in (r - 1, r, r + 1):
                if row < 0 or row >= len(floor_plan):
                    continue
                for col in (c - 1, c, c + 1):
                    if not (col < 0 or col >= len(floor_plan[row]) or (row == r and col == c)):
                        n_occupied_neighbors += 1 if floor_plan[row][col] == Tile.OCCUPIED else 0
            return n_occupied_neighbors

        if floor_plan[r][c] == Tile.FLOOR:
            return False
        elif floor_plan[r][c] == Tile.OCCUPIED:
            return get_n_occupied_neighbors(r, c) >= 4
        else:
            return get_n_occupied_neighbors(r, c) == 0

    return simulate(floor_plan, should_update)


def part2(filepath: str) -> int:
    floor_plan = get_floor_plan(filepath)

    def should_update(floor_plan, r, c):
        def get_n_visible_neighbors(r, c):
            next_pos_in_sightline_funcs = (
                lambda r, c: (r+1, c+1), # up-right diag
                lambda r, c: (r-1, c-1), # down-left diag
                lambda r, c: (r+1, c-1), # up-left diag
                lambda r, c: (r-1, c+1), # down-right diag
                lambda r, c: (r, c+1),  # right
                lambda r, c: (r, c-1), # left
                lambda r, c: (r-1, c), # down
                lambda r, c: (r+1, c)) # up

            n_visible_neighbors = 0
            for next_pos_in_sightline in next_pos_in_sightline_funcs:
                row, col = next_pos_in_sightline(r, c)
                while (row >= 0 and row < len(floor_plan)) and (col >= 0 and col < len(floor_plan[row])):
                    if floor_plan[row][col] == Tile.OCCUPIED:
                        n_visible_neighbors += 1
                        break
                    if floor_plan[row][col] == Tile.EMPTY:
                        break
                    row, col = next_pos_in_sightline(row, col)
            return n_visible_neighbors

        if floor_plan[r][c] == Tile.FLOOR:
            return False
        elif floor_plan[r][c] == Tile.OCCUPIED:
            return get_n_visible_neighbors(r, c) >= 5
        else:
            return get_n_visible_neighbors(r, c) == 0

    return simulate(floor_plan, should_update)


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))


if __name__ == "__main__":
    main()
