txt = [i.strip() for i in open('day24/input.txt').readlines()]

points = []
for line in txt:
    pos, vel = line.split(' @ ')
    x, y, z = [int(i) for i in pos.split(', ')]
    xv, yv, zv = [int(i) for i in vel.split(', ')]
    points.append([[x, y, z], [xv, yv, zv]])


count = 0
for pointIdx1 in range(len(points)):
    for pointIdx2 in range(pointIdx1 + 1, len(points)):
        p1 = points[pointIdx1]
        p1x, p1y, p1z = p1[0]
        p1vx, p1vy, p1vz = p1[1]
        p2 = points[pointIdx2]
        p2x, p2y, p2z = p2[0]
        p2vx, p2vy, p2vz = p2[1]

        # p1: y = p1y + p1vy *t;   x = p1x + p1vx *t
        # p1: y - p1y = p1vy *t;   x - p1x = p1vx *t
        # p1: p1vx(y - p1y) = p1vx * p1vy * t;   p1vy(x - p1x) = p1vx * p1vy * t
        # line 1: p1vx*y - p1vx*p1y = p1vy*x - p1vy*p1x
        # line 1: y = p1y + (p1vy/p1vx)(x - p1x)
        # line 2: y = p2y + (p2vy/p2vx)(x - p2x)

        # cross: p1y + (p1vy/p1vx)(x - p1x) = p2y + (p2vy/p2vx)(x - p2x)
        # cross: p1y + (p1vy/p1vx)x - (p1vy/p1vx)p1x = p2y + (p2vy/p2vx)x - (p2vy/p2vx)p2x
        # cross: (p1vy/p1vx)x - (p2vy/p2vx)x = p2y - p1y - (p2vy/p2vx)p2x + (p1vy/p1vx)p1x
        # cross: (p1vy/p1vx - p2vy/p2vx)x = p2y - p1y - (p2vy/p2vx)p2x + (p1vy/p1vx)p1x
        # cross: x = (p2y - p1y - (p2vy/p2vx)p2x + (p1vy/p1vx)p1x) / (p1vy/p1vx - p2vy/p2vx)
        try:
            x = (p2y - p1y - (p2vy/p2vx)*p2x + (p1vy/p1vx)*p1x) / (p1vy/p1vx - p2vy/p2vx)
        except:
            # print(p1x, p2x)
            # print('parallel')
            continue

        y = p1y + (p1vy/p1vx) * (x - p1x)

        # t1 at intersection: (x - p1x) / (p1vx)
        t1 = (x - p1x) / (p1vx)
        t2 = (x - p2x) / (p2vx)

        inBounds = (200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000)
        # inBounds = (7 <= x <= 27 and 7 <= y <= 27)
        positiveTime = (t1 > 0 and t2 > 0)

        # print(p1x, p2x, t1, t2, x)
        # print(inBounds, positiveTime)

        if inBounds and positiveTime:
            count += 1

print(count)
