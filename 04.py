#! /bin/env python3

import sys
import math
from typing import List, Dict

def get_passports(filepath: str) -> List[Dict[str, str]]:
    with open(filepath) as fin:
        return ({k:v for k,v in p} for p in \
            map(lambda p: (o.split(':') for o in p), \
                map(lambda p: p.replace('\n', ' ').split(' '),
                    fin.read().split("\n\n"))))


def part1(filepath: str) -> int:
    necessary_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    def passport_is_valid(passport: Dict[str, str]) -> bool:
        return not any(map(lambda k: k not in passport, necessary_keys))
    return list(map(lambda p: passport_is_valid(p), get_passports(filepath))).count(True)


def part2(filepath: str) -> int:
    keys_and_validation_predicates = [
        ("byr", lambda b: 1920 <= int(b) <= 2002),
        ("iyr", lambda i: 2010 <= int(i) <= 2020),
        ("eyr", lambda e: 2020 <= int(e) <= 2030),
        ("hgt", lambda h: len(h) > 2 and (59 <= int(h[:-2]) <= 76) if h[-2:] == "in" else (150 <= int(h[:-2]) <= 193) if h[-2:] == "cm" else False),
        ("hcl", lambda h: len(h) == 7 and h[0] == '#' and all(map(lambda s: s in "0123456789abcdef", h[1:]))),
        ("ecl", lambda e: e in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
        ("pid", lambda p: len(p) == 9 and p.isnumeric())]
    def passport_is_valid(passport: Dict[str, str]) -> bool:
        return not any(map(lambda kv: not(kv[0] in passport and kv[1](passport[kv[0]])), keys_and_validation_predicates))
    return list(map(lambda p: passport_is_valid(p), get_passports(filepath))).count(True)


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))

if __name__ == "__main__":
    main()
