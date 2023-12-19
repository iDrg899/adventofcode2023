txt = [i.strip() for i in open('day18/input.txt').readlines()]

field = ['.' * 500 for i in range(500)]

pos = [400, 100]

for line in txt:
    direction, distance, color = line.split()
    distance = int(distance)
    color = color[1:-1]

    if direction == 'U':
        for i in range(pos[0] - 1, pos[0] - distance - 1, -1):
            field[i] = field[i][:pos[1]] + '#' + field[i][pos[1] + 1:]
        pos[0] -= distance
    if direction == 'D':
        for i in range(pos[0] + 1, pos[0] + distance + 1):
            field[i] = field[i][:pos[1]] + '#' + field[i][pos[1] + 1:]
        pos[0] += distance
    if direction == 'L':
        field[pos[0]] = field[pos[0]][:pos[1] - distance] + '#' * distance + field[pos[0]][pos[1]:]
        pos[1] -= distance
    if direction == 'R':
        field[pos[0]] = field[pos[0]][:pos[1] + 1] + '#' * distance + field[pos[0]][pos[1] + distance + 1:]
        pos[1] += distance

for line in field:
    print(line)

# 401 for sample, 399 for input
pointsList = [(399, 101)]
print(field[pointsList[0][0]][pointsList[0][1]])
done = False
lastSearched = 0

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while not done:
    done = True
    for p in pointsList[lastSearched:]:

        for d in directions:
            newPoint = (p[0] + d[0], p[1] + d[1])
            if field[newPoint[0]][newPoint[1]] == '.' and newPoint not in pointsList:
                pointsList.append(newPoint)
                done = False

        lastSearched += 1
    
    if len(pointsList) % 10 == 0:
        print(len(pointsList))
ans = len(pointsList)

for l in field:
    ans += l.count('#')

print(ans)

# 4135 too low