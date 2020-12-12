#! /bin/env python3

import sys
from typing import List, Tuple
from collections import namedtuple
from enum import Enum

Instruction = namedtuple("Instruction", 'opcode operand')
class Op(Enum):
    JMP , ACC, NOP = 0, 1, 2


def get_instructions(filepath: str) -> List[Instruction]:
    op_table = {"jmp": Op.JMP, "acc": Op.ACC, "nop": Op.NOP}
    to_opcode = lambda op: op_table[op]
    return map(lambda sl: Instruction(opcode=to_opcode(sl[0]), operand=int(sl[1])), \
            map(lambda l: l.split(' '), filter(lambda l: len(l) > 0, open(filepath).readlines())))


def execute_instructions(instructions: List[Instruction]) -> Tuple[int, int]:
    have_executed_instruction = [False] * len(instructions)
    acc, pc = 0, 0
    while pc < len(instructions):
        if have_executed_instruction[pc]:
            break
        have_executed_instruction[pc] = True

        instruction = instructions[pc]
        if instruction.opcode == Op.ACC:
            acc += instruction.operand
        elif instruction.opcode == Op.JMP:
            pc += instruction.operand - 1
        pc += 1
    return acc, pc


def part1(filepath: str) -> int:
    return execute_instructions(list(get_instructions(filepath)))[0]


def part2(filepath: str) -> int:
    instructions = list(get_instructions(filepath))

    op_transform_table = {Op.NOP: Op.JMP, Op.JMP: Op.NOP, Op.ACC: Op.ACC}
    for i, instruction in enumerate(instructions):
        instructions[i] = Instruction(opcode=op_transform_table[instruction.opcode], operand=instruction.operand)
        acc, pc = execute_instructions(instructions)
        if pc >= len(instructions):
            return acc
        instructions[i] = instruction


def main():
    if len(sys.argv) >= 3:
        print((part1, part2)[int(sys.argv[2]) - 1](sys.argv[1]))


if __name__ == "__main__":
    main()
