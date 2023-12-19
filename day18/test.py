txt = [i.strip() for i in open('day18/input.txt').readlines()]

field = ['.' * 100 for i in range(100)]

pos = [0, 0]

minx = 0
maxx = 0
miny = 0
maxy = 0

for line in txt:
    direction, distance, color = line.split()
    distance = int(distance)
    color = color[1:-1]

    if direction == 'U':
        pos[0] -= distance
    if direction == 'D':
        pos[0] += distance
    if direction == 'L':
        pos[1] -= distance
    if direction == 'R':
        pos[1] += distance

    if pos[0] < miny:
        miny = pos[0]
    if pos[0] > maxy:
        maxy = pos[0]
    if pos[1] < minx:
        minx = pos[1]
    if pos[1] > maxx:
        maxx = pos[1]

    print(miny, maxy, minx, maxx)