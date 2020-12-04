#! /bin/env python3

import sys
from typing import Tuple, Callable

def parse_line(line: str) -> Tuple[int, int, str, str]:
    numbers, letter, password = line.split(' ')
    number1, number2 = (int(x) for x in numbers.split('-'))
    letter = letter[0]
    return number1, number2, letter, password


def n_parsed_lines_matched(filepath: str, predicate_func: Callable[[int, int, str, str], int]) -> int:
    with open(filepath) as fin:
        return list(map(lambda x: predicate_func(*parse_line(x)), fin.readlines())).count(True)


def part1(filepath: str) -> int:
    def password_is_valid(at_least: int, at_most: int, letter: str, password: str) -> bool:
        return at_least <= password.count(letter) <= at_most
    return n_parsed_lines_matched(filepath, password_is_valid)


def part2(filepath: str) -> int:
    def password_is_valid(idx1: int, idx2: int, letter: str, password: str) -> bool:
        idx1_has_letter = 0 <= idx1 - 1 < len(password) and password[idx1 - 1] == letter
        idx2_has_letter = 0 <= idx2 - 1 < len(password) and password[idx2 - 1] == letter
        return (idx1_has_letter and not idx2_has_letter) or (idx2_has_letter and not idx1_has_letter)
    return n_parsed_lines_matched(filepath, password_is_valid)


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))


if __name__ == "__main__":
    main()
