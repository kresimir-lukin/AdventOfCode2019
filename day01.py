import sys

assert len(sys.argv) == 2
masses = list(map(int, open(sys.argv[1]).read().split()))

part1 = part2 = 0
for mass in masses:
    mass = mass//3 - 2
    part1 += mass
    while mass > 0:
        part2 += mass
        mass = mass//3 - 2

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))