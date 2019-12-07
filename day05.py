import sys, intcode

assert len(sys.argv) == 2
code = list(map(int, open(sys.argv[1]).read().split(',')))

def execute(code, system_id):
    program = intcode.IntCode(code, [system_id])
    last_output, halted = None, False
    while not halted:
        last_output = program.output
        halted = program.run()
    return last_output

part1 = execute(code, 1)
part2 = execute(code, 5)

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))