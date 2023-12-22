txt = [i.strip() for i in open('day22/input.txt').readlines()]

bricks = []

for brickId in range(len(txt)):
    point1, point2 = [[int(i) for i in coords.split(',')] for coords in txt[brickId].split('~')]
    bricks.append([point1, point2, brickId])

bricks.sort(key=lambda x: x[0][2])

heightMap = []
size = 10
for y in range(size):
    l = []
    for z in range(size):
        l.append(0)
    heightMap.append(l)

topMap = []
for y in range(size):
    l = []
    for z in range(size):
        l.append(None)
    topMap.append(l)

supporting = {brick[2]: [] for brick in bricks}
supporters = {brick[2]: [] for brick in bricks}

for brick in bricks:

    point1 = brick[0]
    point2 = brick[1]
    brickId = brick[2]

    x1, y1, z1 = point1
    x2, y2, z2 = point2

    # A cheat
    z1 += 1
    z2 += 1
    landed = False

    while not landed:
        z1 -= 1
        z2 -= 1

        if z1 <= 1:
            landed = True
            break

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if z1 <= 1 + heightMap[y][x]:
                    landed = True
                    if topMap[y][x] not in supporters[brickId]:
                        supporters[brickId].append(topMap[y][x])
                    if brickId not in supporting[topMap[y][x]]:
                        supporting[topMap[y][x]].append(brickId)

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            heightMap[y][x] = z2
            topMap[y][x] = brickId


def topple(brickId, toppled):
    toppleNumber = 0

    for hat in supporting[brickId]:

        dead = True
        for boot in supporters[hat]:
            if boot not in toppled:
                dead = False

        if dead:
            toppled.append(hat)
            toppleNumber += 1 + topple(hat, toppled)

    return toppleNumber

answer = 0

for brickId in range(len(bricks)):
    answer += topple(brickId, [brickId])

print(answer)
