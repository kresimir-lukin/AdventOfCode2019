import sys, intcode

assert len(sys.argv) == 2
code = list(map(int, open(sys.argv[1]).read().split(',')))

def execute(code, noun, verb):
    program = intcode.IntCode(code, [])
    program.update(1, noun)
    program.update(2, verb)
    program.run()
    return program.get(0)

part1 = execute(code, 12, 2)
part2 = next(100*noun + verb for noun in range(100) for verb in range(100) if execute(code, noun, verb) == 19690720)

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))