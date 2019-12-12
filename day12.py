import sys, math, re

def parse_point(str):
    match = re.match('<x=(-?[0-9]+), y=(-?[0-9]+), z=(-?[0-9]+)>', str)
    return (int(match[1]), int(match[2]), int(match[3]))

def run_simulation(positions, velocities, steps=float('inf')):
    original_positions, original_velocities = positions[:], velocities[:]
    step_number = 0
    while step_number < steps and (not step_number or positions != original_positions or velocities != original_velocities):
        for i in range(len(positions)):
            velocities[i] += sum(1 if positions[i] < position else -1 for position in positions if position != positions[i])
        for i in range(len(positions)):
            positions[i] += velocities[i]
        step_number += 1
    return step_number

def part1(positions):
    px, vx = [x for x, _, _ in positions], [0] * len(positions)
    py, vy = [y for _, y, _ in positions], [0] * len(positions)
    pz, vz = [z for _, _, z in positions], [0] * len(positions)
    for p, v in zip((px, py, pz), (vx, vy, vz)):
        run_simulation(p, v, 1000)
    return sum((abs(px[i]) + abs(py[i]) + abs(pz[i])) * (abs(vx[i]) + abs(vy[i]) + abs(vz[i])) for i in range(len(positions)))

def part2(positions):
    def _lcm(a, b):
        return a * b // math.gcd(a, b)
    steps_x = run_simulation([x for x, _, _ in positions], [0] * len(positions))
    steps_y = run_simulation([y for _, y, _ in positions], [0] * len(positions))
    steps_z = run_simulation([z for _, _, z in positions], [0] * len(positions))
    return _lcm(_lcm(steps_x, steps_y), steps_z)

assert len(sys.argv) == 2
moon_positions = list(map(parse_point, open(sys.argv[1]).read().split('\n')))

print('Part 1: {0}, Part 2: {1}'.format(part1(moon_positions), part2(moon_positions)))