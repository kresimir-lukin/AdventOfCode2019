import sys, intcode

assert len(sys.argv) == 2
code = list(map(int, open(sys.argv[1]).read().split(',')))

part1 = intcode.IntCode(code, [1]).execute()
part2 = intcode.IntCode(code, [2]).execute()

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))