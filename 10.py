#! /bin/env python3

import sys
from typing import List
from collections import Counter, defaultdict

def get_adapters(filepath: str) -> List[int]:
    return map(lambda n: int(n), open(filepath).readlines())


def part1(filepath: str) -> int:
    current_joltage = 0
    joltage_difference_counts = [0, 0, 0, 1]
    for adapter in sorted(get_adapters(filepath)):
        joltage_difference_counts[adapter - current_joltage] += 1
        current_joltage = adapter
    return joltage_difference_counts[1] * joltage_difference_counts[3]


def part2(filepath: str) -> int:
    highest_joltage_adapter = max(get_adapters(filepath))
    adapter_counts = Counter(get_adapters(filepath))
    memo = defaultdict(lambda: defaultdict(lambda: -1))

    def serialize_counts():
        return ",".join(map(lambda k: f"{k}:{adapter_counts[k]}", \
                sorted(filter(lambda k: adapter_counts[k] > 0, adapter_counts.keys()))))

    def number_ways(joltage):
        if joltage == highest_joltage_adapter:
            return 1

        serialized_counts = serialize_counts
        memoized = memo[joltage][serialized_counts]
        if memoized != -1:
            return memoized

        total_n_ways = 0
        for joltage_offset in range(0, 4):
            next_joltage = joltage + joltage_offset
            adapter_count_for_next_joltage = adapter_counts[next_joltage]
            if adapter_count_for_next_joltage > 0:
                adapter_counts[next_joltage] -= 1
                total_n_ways += number_ways(next_joltage)
                adapter_counts[next_joltage] += 1
        memo[joltage][serialized_counts] = total_n_ways
        return total_n_ways

    return number_ways(0)


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))


if __name__ == "__main__":
    main()
