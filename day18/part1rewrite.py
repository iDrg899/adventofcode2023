txt = [i.strip() for i in open('day18/input.txt').readlines()]

directions = {'R':[0,  1],
              'D':[1,  0],
              'L':[0, -1],
              'U':[-1, 0]
              }

pos = [0, 0]
oldx, oldy = 0, 0

area = 0
perimeter = 0

for line in txt:
    direction, distance, color = line.split()
    distance = int(distance)

    v = directions[direction]

    pos[0] += v[0] * distance
    pos[1] += v[1] * distance
    y, x = pos[0], pos[1]

    area += oldx * y
    area -= oldy * x

    perimeter += distance

    oldx, oldy = x, y

print((area + perimeter) // 2 + 1)