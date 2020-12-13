#! /bin/env python3

import sys
from typing import List, Tuple
from collections import defaultdict

def get_nums(filepath: str) -> List[int]:
    return map(lambda n: int(n), open(filepath).readlines())


def part1(filepath: str) -> int:
    def two_sum(arr: List[int], target: int) -> bool:
        have = defaultdict(lambda: False)
        for i in arr:
            need = target - i
            if have[need]:
                return True
            have[i] = True

    q = []
    for n in get_nums(filepath):
        if len(q) < 25:
            q.append(n)
            continue

        if not two_sum(q, n):
            return n

        q.pop(0)
        q.append(n)


def part2(filepath: str) -> int:
    target = part1(filepath)
    nums = list(get_nums(filepath))
    sub_arr_sum = 0
    l, r = 0, 0

    while l < len(nums):
        if sub_arr_sum < target:
            sub_arr_sum += nums[r]
            r += 1
        elif sub_arr_sum > target:
            sub_arr_sum -= nums[l]
            l += 1
        else:
            sub_arr = nums[l:r+1]
            return max(sub_arr) + min(sub_arr)


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))


if __name__ == "__main__":
    main()
