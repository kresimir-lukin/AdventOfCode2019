import sys

assert len(sys.argv) == 2
program = list(map(int, open(sys.argv[1]).read().split(',')))

def execute(program, noun, verb):
    program = program[:]
    program[1:3] = noun, verb
    pc = instruction = 0
    while instruction != 99:
        instruction, from1, from2, to = program[pc:pc+4]
        if instruction == 1:
            program[to] = program[from1] + program[from2]
        elif instruction == 2:
            program[to] = program[from1] * program[from2]
        pc += 4
    return program[0]

part1 = execute(program, 12, 2)
part2 = next(100*noun + verb for noun in range(100) for verb in range(100) if execute(program, noun, verb) == 19690720)

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))