txt = [i.strip() for i in open('day18/input.txt').readlines()]

directions = {0:[0,  1],
              1:[1,  0],
              2:[0, -1],
              3:[-1, 0]
              }

pos = [0, 0]
oldx, oldy = 0, 0

area = 0
perimeter = 0

for line in txt:
    info = line.split()[2][2:-1]
    distance, direction = int(info[0:5], 16), int(info[5])

    v = directions[direction]

    pos[0] += v[0] * distance
    pos[1] += v[1] * distance
    y, x = pos[0], pos[1]

    area += oldx * y
    area -= oldy * x

    perimeter += distance

    oldx, oldy = x, y

print((area + perimeter) // 2 + 1)