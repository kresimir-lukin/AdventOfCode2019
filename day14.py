import sys, math

def parse_input(lines):
    def _parse_numsymbol(numsymbol):
        num, symbol = numsymbol.strip().split()
        return symbol, int(num)
    reactions = {}
    for line in lines:
        left, right = line.split('=>')
        left, right = list(map(_parse_numsymbol, left.split(','))), _parse_numsymbol(right)
        reactions[right[0]] = (right[1], left)
    return reactions

def ensure(reactions, data, what, howmuch):
    if data[what] >= howmuch:
        return True
    if what == 'ORE':
        return False
    n = math.ceil((howmuch - data[what]) / reactions[what][0])
    ensured = True
    for sub_what, sub_howmuch in reactions[what][1]:
        ensured = ensured and ensure(reactions, data, sub_what, n*sub_howmuch)
        data[sub_what] -= n*sub_howmuch
    if ensured:
        data[what] += n*reactions[what][0]
    return ensured

def part1(reactions):
    low, high = 0, 10**12
    while low < high:
        mid = low + (high - low) // 2
        data = {element: 0 for element in reactions}
        data['ORE'] = mid
        if ensure(reactions, data, 'FUEL', 1):
            high = mid
        else:
            low = mid + 1
    return low

def part2(reactions):
    low, high = 0, 10**12
    while low < high-1:
        mid = low + (high - low) // 2
        data = {element: 0 for element in reactions}
        data['ORE'] = 10**12
        if ensure(reactions, data, 'FUEL', mid):
            low = mid
        else:
            high = mid - 1
    return high if ensure(reactions, data, 'FUEL', high) else low

assert len(sys.argv) == 2
reactions = parse_input(open(sys.argv[1]).read().split('\n'))

print('Part 1: {0}, Part 2: {1}'.format(part1(reactions), part2(reactions)))