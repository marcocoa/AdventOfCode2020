#! /bin/env python3

import sys
from typing import List, Tuple, Dict
from collections import defaultdict, namedtuple

BagData = namedtuple("BagData", 'color count')


def create_graph(filepath: str) -> Dict[str, List[BagData]]:
    def parse_line(line: str) -> Tuple[str, List[BagData]]:
        normalized_split_line = line.strip().replace("bags", '').replace("bag", '').replace('.', '').split(' ')
        bag_color = ' '.join(normalized_split_line[0:2])

        if "no other bags" in line:
            return (bag_color, [])

        sub_bags = map(lambda b: BagData(count=int(b[0]), color=' '.join(b[1:]).strip()), \
                map(lambda b: b.strip().split(' '), ' '.join(normalized_split_line[4:]).split(',')))
        return (bag_color, list(sub_bags))

    with open(filepath) as fin:
        graph = {}
        for line in fin:
            bag_color, sub_bags = parse_line(line)
            graph[bag_color] = sub_bags
        return graph


def part1(filepath: str) -> int:
    UNSEARCHED = 0
    CONTAINS_KEY = 1
    DOESNT_CONTAIN_KEY = 2

    graph = create_graph(filepath)
    memo = defaultdict(lambda: UNSEARCHED)

    def dfs(bag: str) -> bool:
        for sub_bag in graph[bag]:
            if sub_bag.color == "shiny gold":
                return True

            status = memo[sub_bag.color]
            if status == CONTAINS_KEY:
                return True
            elif status == UNSEARCHED:
                contains_key = dfs(sub_bag.color)
                if contains_key:
                    memo[sub_bag.color] = CONTAINS_KEY
                    return True
                memo[sub_bag.color] = DOESNT_CONTAIN_KEY
        return False

    for bag in graph.keys():
        if memo[bag] == UNSEARCHED:
            contains_key = dfs(bag)
            memo[bag] = CONTAINS_KEY if contains_key else DOESNT_CONTAIN_KEY

    return len(list(filter(lambda k: memo[k] == CONTAINS_KEY, memo.keys())))


def part2(filepath: str) -> int:
    UNSEARCHED = -1
    graph = create_graph(filepath)
    memo = defaultdict(lambda: UNSEARCHED)

    def dfs(bag: str) -> int:
        total_sub_bag_sum = 0
        for sub_bag in graph[bag]:
            memoized = memo[sub_bag.color]

            sub_bag_sum = memoized if memoized != -1 else dfs(sub_bag.color)
            memo[sub_bag.color] = sub_bag_sum
            total_sub_bag_sum += sub_bag.count * sub_bag_sum
        return 1 + total_sub_bag_sum
    return dfs("shiny gold") - 1


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))


if __name__ == "__main__":
    main()
