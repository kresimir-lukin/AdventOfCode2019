import sys, intcode

def part1(code):
    program = intcode.IntCode(code)
    halted, blocks = False, 0
    while not halted:
        program.run()
        program.run()
        halted, blocktype = program.run()
        blocks += blocktype == 2
    return blocks

def part2(code):
    ball_x = paddle_x = None
    program = intcode.IntCode(code, [], lambda: (ball_x > paddle_x) - (ball_x < paddle_x))
    program.set(0, 2)
    halted, last_points = False, 0
    while not halted:
        _, x = program.run()
        _, y = program.run()
        halted, blocktype = program.run()
        if not halted:
            paddle_x = x if blocktype == 3 else paddle_x
            ball_x = x if blocktype == 4 else ball_x
            last_points = blocktype if (x, y) == (-1, 0) else last_points
    return last_points

assert len(sys.argv) == 2
code = list(map(int, open(sys.argv[1]).read().split(',')))

print('Part 1: {0}, Part 2: {1}'.format(part1(code), part2(code)))