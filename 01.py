#! /bin/env python3

from collections import defaultdict
import sys

def part1(filepath: str) -> int:
    with open(filepath) as fin:
        have_cache = defaultdict(lambda: False)
        for n_str in fin:
            have = int(n_str)
            need = 2020 - have
            if have_cache[need]:
                return have * need
            have_cache[have] = True


def part2(filepath: str) -> int:
    with open(filepath) as fin:
        numbers = sorted(map(lambda x: int(x), fin.readlines()))

    for i in range(len(numbers) - 2):
        j = i + 1
        k = len(numbers) - 1

        while j < k:
            three_sum = numbers[i] + numbers[j] + numbers[k]
            if three_sum < 2020:
                j += 1
            elif three_sum > 2020:
                k -= 1
            else:
                return three_sum


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))


if __name__ == "__main__":
    main()
