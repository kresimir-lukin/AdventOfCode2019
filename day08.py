import sys

assert len(sys.argv) == 2
data = open(sys.argv[1]).read()

def build_layers(data):
    layers, n = [], width * height
    for i in range(len(data) // n):
        layers.append([list(map(int, data[i*n + j*width : i*n + (j+1)*width])) for j in range(height)])
    return layers

def count_pixels(image, x):
    return sum(1 for row in image for col in row if col == x)

width, height = 25, 6
layers = build_layers(data)

_, layer = min((count_pixels(layer, 0), layer) for layer in layers)
part1 = count_pixels(layer, 1) * count_pixels(layer, 2)

image = [['#']*width for _ in range(height)]
for r in range(height):
    for c in range(width):
        pixel = next(layer[r][c] for layer in layers if layer[r][c] != 2)
        image[r][c] = '*' if pixel == 1 else ' '
part2 = '\n'.join(''.join(row) for row in image)

print('Part 1: {0}, Part 2: \n{1}'.format(part1, part2))