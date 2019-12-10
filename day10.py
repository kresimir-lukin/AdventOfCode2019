import sys, math

assert len(sys.argv) == 2
asteroid_map = open(sys.argv[1]).read().split()
asteroid_coordinates = [(x, y) for y, row in enumerate(asteroid_map) for x, value in enumerate(row) if value == '#']

def get_monitoring_point(coordinates):
    max_asteroids = 0
    best_x = best_y = 0
    for x, y in asteroid_coordinates:
        point_slopes = set()
        for x2, y2 in asteroid_coordinates:
            if (x, y) != (x2, y2):
                dx, dy = x2 - x, y2 - y
                dx, dy = dx // math.gcd(dx, dy), dy // math.gcd(dx, dy)
                point_slopes.add((dx, dy))
        if len(point_slopes) > max_asteroids:
            max_asteroids = len(point_slopes)
            best_x, best_y = x, y
    return max_asteroids, (best_x, best_y)

def get_vaporization_order(coordinates, mx, my):
    vaporized = [(mx, my)]
    while len(vaporized) != len(coordinates):
        closest_points = {}
        for x, y in coordinates:
            if (x, y) not in vaporized:
                dx, dy = x - mx, y - my
                dx, dy = dx // math.gcd(dx, dy), dy // math.gcd(dx, dy)
                closestx, closesty = closest_points.get((dx, dy), (float('inf'), float('inf')))
                if abs(x - mx) + abs(y - my) < abs(closestx - mx) + abs(closesty - my):
                    closest_points[(dx, dy)] = (x, y)
        vaporized += sorted(closest_points.values(), key=lambda p:-math.atan2(p[0] - mx, p[1] - my))
    return vaporized

part1, monitoring_p = get_monitoring_point(asteroid_coordinates)
vaporization_order = get_vaporization_order(asteroid_coordinates, monitoring_p[0], monitoring_p[1])
part2 = vaporization_order[200][0] * 100 + vaporization_order[200][1]

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))