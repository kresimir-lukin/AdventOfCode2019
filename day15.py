import sys, collections, intcode

def discover_map(code):
    queue = collections.deque([(0, 0)])
    seen = {(0, 0): intcode.IntCode(code)}
    fill = ['#', '.', 'O']
    points = {}
    while queue:
        x, y = queue.pop()
        for direction, dx, dy in [(1, 0, -1), (2, 0, 1), (3, -1, 0), (4, 1, 0)]:
            xx, yy = x + dx, y + dy
            if (xx, yy) not in seen:
                program = seen[(x, y)].clone()
                program.input(direction)
                output = program.run()
                seen[(xx, yy)] = program
                points[(xx, yy)] = fill[output]
                if output != 0:
                    queue.appendleft((xx, yy))
    return points

def part1(points):
    queue = collections.deque([(0, 0, 0)])
    seen = set()
    steps_to_O = None
    while queue and steps_to_O is None:
        steps, x, y = queue.pop()
        seen.add((x, y))
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            xx, yy = x + dx, y + dy
            if (xx, yy) not in seen:
                point = points.get((xx, yy), '#')
                if point == 'O':
                    steps_to_O = steps+1
                if point != '#':
                    queue.appendleft((steps+1, xx, yy))
    return steps_to_O

def part2(points):
    Ox, Oy = next((x, y) for (x, y), val in points.items() if val == 'O')
    queue = [(Ox, Oy)]
    seen = set()
    minutes = -1
    while queue:
        queue_next_minute = []
        while queue:
            x, y = queue.pop()
            seen.add((x, y))
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                xx, yy = x + dx, y + dy
                if (xx, yy) not in seen and points.get((xx, yy), '#') == '.':
                    queue_next_minute.append((xx, yy))
        queue = queue_next_minute
        minutes += 1
    return minutes

assert len(sys.argv) == 2
code = list(map(int, open(sys.argv[1]).read().split(',')))

map_points = discover_map(code)

print('Part 1: {0}, Part 2: {1}'.format(part1(map_points), part2(map_points)))