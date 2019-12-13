import sys, intcode, itertools

assert len(sys.argv) == 2
code = list(map(int, open(sys.argv[1]).read().split(',')))

part1 = 0
for phases in itertools.permutations(range(5)):
    programs = [intcode.IntCode(code, [phases[i]]) for i in range(5)]
    previous_output = 0
    for program in programs:
        program.input(previous_output)
        previous_output = program.execute()
    part1 = max(part1, previous_output)

part2 = 0
for phases in itertools.permutations(range(5, 10)):
    programs = [intcode.IntCode(code, [phases[i]]) for i in range(5)]
    halted, previous_output = False, 0
    while not halted:
        for program in programs:
            program.input(previous_output)
            halted, output = program.run()
            previous_output = output if output is not None else previous_output
    part2 = max(part2, previous_output)

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))