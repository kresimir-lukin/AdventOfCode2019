import sys, intcode

def paint_execute(code, initial_color):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    program = intcode.IntCode(code)
    x = y = direction = 0
    panel = { (x, y): initial_color }
    while not program.halted:
        program.input(panel[(x, y)] if (x, y) in panel else 0)
        output1 = program.run()
        output2 = program.run()
        if not program.halted:
            panel[(x, y)] = output1
            direction = ((direction + 1) if output2 == 1 else (direction - 1 + len(directions))) % len(directions)
            x, y = x + directions[direction][0], y + directions[direction][1]
    return panel

def build_registration(panel_points):
    registration = [[' ']*40 for _ in range(6)]
    for row in range(6):
        for col in range(40):
            if panel_points.get((col, row), 0) == 1:
                registration[row][col] = '*'
    return '\n'.join(''.join(row) for row in registration)

code = list(map(int, open(sys.argv[1]).read().split(',')))

part1 = len(paint_execute(code, 0))
part2 = build_registration(paint_execute(code, 1))

print('Part 1: {0}, Part 2: \n{1}'.format(part1, part2))