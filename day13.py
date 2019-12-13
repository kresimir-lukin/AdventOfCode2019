import sys, intcode

def part1(code):
    program = intcode.IntCode(code)
    blocks = 0
    while not program.halted:
        program.run()
        program.run()
        blocktype = program.run()
        blocks += blocktype == 2
    return blocks

def part2(code):
    ball_x = paddle_x = None
    program = intcode.IntCode(code, [], lambda: (ball_x > paddle_x) - (ball_x < paddle_x))
    program.set(0, 2)
    last_points = 0
    while not program.halted:
        x = program.run()
        y = program.run()
        blocktype = program.run()
        if not program.halted:
            paddle_x = x if blocktype == 3 else paddle_x
            ball_x = x if blocktype == 4 else ball_x
            last_points = blocktype if (x, y) == (-1, 0) else last_points
    return last_points

assert len(sys.argv) == 2
code = list(map(int, open(sys.argv[1]).read().split(',')))

print('Part 1: {0}, Part 2: {1}'.format(part1(code), part2(code)))