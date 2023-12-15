txt = [i.strip() for i in open('day14/input.txt').readlines()]

length = len(txt)
balls = []
walls = []

for li in range(length):
    for i in range(length):
        if txt[li][i] == 'O':
            balls.append((li, i))
        if txt[li][i] == '#':
            walls.append((li, i))

# balls.sort(key = lambda x: x[1])

ballsList = []

doneish = False
i = 0
while i < 1000000000:
    # North:
    balls.sort()
    for bi in range(len(balls)):
        b = balls[bi]
        if b[0] == 0:
            continue
        while (b[0] - 1, b[1]) not in walls and (b[0] - 1, b[1]) not in balls and b[0] > 0:
            b = balls[bi] = (b[0] - 1, b[1])

    # West:
    balls.sort(key = lambda x: x[1])
    for bi in range(len(balls)):
        b = balls[bi]
        if b[1] == 0:
            continue
        while (b[0], b[1] - 1) not in walls and (b[0], b[1] - 1) not in balls and b[1] > 0:
            b = balls[bi] = (b[0], b[1] - 1)

    # South:
    balls.sort(key = lambda x: -x[0])
    for bi in range(len(balls)):
        b = balls[bi]
        if b[0] == length - 1:
            continue
        while (b[0] + 1, b[1]) not in walls and (b[0] + 1, b[1]) not in balls and b[0] < length - 1:
            b = balls[bi] = (b[0] + 1, b[1])

    # East:
    balls.sort(key = lambda x: -x[1])
    for bi in range(len(balls)):
        b = balls[bi]
        if b[1] == length - 1:
            continue
        while (b[0], b[1] + 1) not in walls and (b[0], b[1] + 1) not in balls and b[1] < length - 1:
            b = balls[bi] = (b[0], b[1] + 1)

    if balls in ballsList and doneish == False:
        doneish = True
        print('repeat at', i)
        # print('at', ballsList.index(balls))
        i += (i - ballsList.index(balls)) * ((1000000000 - i) // (i - ballsList.index(balls)))
    ballsList.append([i for i in balls])

    print(i)

    i += 1
print(sum([length - b[0] for b in balls]))