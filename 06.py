#! /bin/env python3

import sys
from collections import Counter

def part1(filepath: str) -> int:
    return sum(map(lambda g: len(set(g)), map(lambda g: "".join(g).replace("\n", ""), filter(lambda x: x!= "", open(filepath).read().split("\n\n")))))


def part2(filepath: str) -> int:
    return sum(map(lambda x: len(list(x)), map(lambda c: filter(lambda k: c[k] == c['\n'] + 1, c), map(lambda g: Counter(g), filter(lambda x: x!= "", open(filepath).read().split("\n\n"))))))


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))


if __name__ == "__main__":
    main()
