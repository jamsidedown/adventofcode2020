import re
from typing import Callable, Dict, List, Set


pattern = re.compile(r'^(\w{3}) ([+-]\d+)')


class Instr:
    def __init__(self, line: str):
        if match := pattern.match(line):
            opcode, value = match.groups()
            self.opcode = opcode
            self.value = int(value)
        else:
            raise TypeError()

class Vm:
    def __init__(self, instructions: List[Instr]):
        self.instructions = instructions
        self.ptr = 0
        self.acc = 0
        self.ptrs: Set[int] = set()
        self.looped = False

    def step(self):
        instr = self.instructions[self.ptr]
        if instr.opcode == 'nop':
            self.ptr += 1
        elif instr.opcode == 'acc':
            self.acc += instr.value
            self.ptr += 1
        elif instr.opcode == 'jmp':
            self.ptr += instr.value

    def run(self) -> int:
        while True:
            if self.ptr >= len(self.instructions):
                return self.acc
            if self.ptr in self.ptrs:
                self.looped = True
                return self.acc
            self.ptrs.add(self.ptr)
            self.step()


class Vm2:
    def __init__(self, instructions: List[Instr]):
        self.instructions = instructions
        self.ptr = 0
        self.acc = 0
        self.ptrs: Set[int] = set()
        self.looped = False
        self.ops: Dict[str, Callable[[int], None]] = {
            'nop': self._nop,
            'acc': self._acc,
            'jmp': self._jmp,
        }

    def run(self) -> int:
        while True:
            if self.ptr >= len(self.instructions):
                return self.acc

            if self.ptr in self.ptrs:
                self.looped = True
                return self.acc

            self.step()

    def step(self):
        self.ptrs.add(self.ptr)
        instr = self.instructions[self.ptr]
        self.ops[instr.opcode](instr.value)

    def _nop(self, value: int) -> None:
        self.ptr += 1

    def _acc(self, value: int) -> None:
        self.acc += value
        self.ptr += 1

    def _jmp(self, value: int) -> None:
        self.ptr += value


def part_1(instructions: List[Instr]) -> int:
    vm = Vm(instructions)
    return vm.run()


def part_2(instructions: List[Instr]) -> int:
    for i in range(len(instructions)):
        instr = instructions[i]
        start_op = instr.opcode
        swapcode = {'jmp': 'nop', 'nop': 'jmp'}
        if not start_op in swapcode:
            continue
        instr.opcode = swapcode[start_op]
        vm = Vm(instructions)
        value = vm.run()
        if not vm.looped:
            return value
        instr.opcode = start_op
    return 0


def parse(filename: str) -> List[Instr]:
    with open(filename, 'r') as f:
        return [Instr(line) for line in f]


if __name__ == '__main__':
    instructions = parse('day_08/input.txt')
    print(f'Acc value when program looped: {part_1(instructions)}')
    print(f'Acc value when program fixed: {part_2(instructions)}')
