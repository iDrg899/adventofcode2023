import math

txt = [i.strip() for i in open('day24/input.txt').readlines()]

points = []
for line in txt:
    pos, vel = line.split(' @ ')
    x, y, z = [int(i) for i in pos.split(', ')]
    xv, yv, zv = [int(i) for i in vel.split(', ')]
    points.append([[x, y, z], [xv, yv, zv]])

parallelPairs = []

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

        # try:
        #     x = (p2y - p1y - (p2vy/p2vx)*p2x + (p1vy/p1vx)*p1x) / (p1vy/p1vx - p2vy/p2vx)
        # except:
        #
        if p1vy/p1vx == p2vy/p2vx and p1vz/p1vx == p2vz / p2vx:
            parallelPairs.append([p1, p2])
            print(p1vy/p1vx)
            print('parallel')


        # y = p1y + (p1vy/p1vx) * (x - p1x)

        # # t1 at intersection: (x - p1x) / (p1vx)
        # t1 = (x - p1x) / (p1vx)
        # t2 = (x - p2x) / (p2vx)

        # inBounds = (200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000)
        # # inBounds = (7 <= x <= 27 and 7 <= y <= 27)
        # positiveTime = (t1 > 0 and t2 > 0)

        # # print(p1x, p2x, t1, t2, x)
        # # print(inBounds, positiveTime)

        # if inBounds and positiveTime:
        #     count += 1

print(count)


def crossProduct(a, b):
    a1, a2, a3 = a
    b1, b2, b3 = b
    return [a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1]

pair1 = parallelPairs[0]
pair2 = parallelPairs[2]

planeNormalVectors = []
planeConstants = []
for pair in [pair1, pair2]:
    print('pair:',pair)
    p1 = pair[0]
    p2 = pair[1]
    p1x, p1y, p1z = p1[0]
    p1vx, p1vy, p1vz = p1[1]
    p2x, p2y, p2z = p2[0]
    p2vx, p2vy, p2vz = p2[1]

    someVectorFromOneLineToTheOther = [p2x - p1x, p2y - p1y, p2z - p1z]
    print('sv:', someVectorFromOneLineToTheOther)
    directionVector = [p1vx, p1vy, p1vz]

    normalVector = crossProduct(someVectorFromOneLineToTheOther, directionVector)

    planeNormalVectors.append(normalVector)
    planeConstants.append(normalVector[0] * p1x + normalVector[1] * p1y + normalVector[2] * p1z)

print(planeNormalVectors[0], planeNormalVectors[1])
directionVector = crossProduct(planeNormalVectors[0], planeNormalVectors[1])

print(directionVector)
scaleFactor = math.gcd(directionVector[0], directionVector[1], directionVector[2])
scaledDirectionVector = [i//scaleFactor for i in directionVector]
print()
print(scaledDirectionVector, 'ඞඞඞඞඞ')

# Find point on the line with x = 0
# 1) planeNormalVectors[0][1] * y + planeNormalVectors[0][2] * z = planeConstants[0]
# 2) planeNormalVectors[1][1] * y + planeNormalVectors[1][2] * z = planeConstants[1]
# 1) planeNormalVectors[0][1] * planeNormalVectors[1][1] * y + planeNormalVectors[0][2] * planeNormalVectors[1][1] * z = planeConstants[0] * planeNormalVectors[1][1]
# 2) planeNormalVectors[1][1] * planeNormalVectors[0][1] * y + planeNormalVectors[1][2] * planeNormalVectors[0][1] * z = planeConstants[1] * planeNormalVectors[0][1]
# subtract: z * (planeNormalVectors[0][2] * planeNormalVectors[1][1] - planeNormalVectors[1][2] * planeNormalVectors[0][1]) = planeConstants[0] * planeNormalVectors[1][1] - planeConstants[1] * planeNormalVectors[0][1]
print(planeConstants[0], planeNormalVectors[0])
x0 = 0
z0 = (planeConstants[0] * planeNormalVectors[1][1] - planeConstants[1] * planeNormalVectors[0][1]) / (planeNormalVectors[0][2] * planeNormalVectors[1][1] - planeNormalVectors[1][2] * planeNormalVectors[0][1])
y0 = (planeConstants[0] - planeNormalVectors[0][2] * z0) / planeNormalVectors[0][1]
print(x0, y0, z0, 'ඞඞඞ')



# Intersection point of the line we found with p1 and p2

p1 = points[0]
p2 = points[1]
p1x, p1y, p1z = p1[0]
p1vx, p1vy, p1vz = p1[1]
p2x, p2y, p2z = p2[0]
p2vx, p2vy, p2vz = p2[1]

vx, vy, vz = directionVector

# Reparametrize:
# line 1: (p1x + p1vx * t, p1y + p1vy * t, p1z + p1vz * t)
# line 0: (x0 + vx * p,    y0 + vy * p,    z0 + vz * p)
# p1x + p1vx * t = x0 + vx * p
# p = (p1x - x0 + p1vx * t) / vx

# x0 + vx * p = p1x
# y0ñ = y0 + vy * p
# y0ñ = y0 + vy * (p1x - x0) / vx
y0ñ = y0 + vy/vx * (p1x - x0)
z0ñ = z0 + vz/vx * (p1x - x0)

y0ŋ = y0 + vy/vx * (p2x - x0)
z0ŋ = z0 + vz/vx * (p2x - x0)

# line 0: (p1x + p1vx * t, y0ñ + vy * t, z0ñ + vz * t)

# Find intersection:
# p1y + p1vy * t = y0ñ + vy * t
# (p1vy - vy) * t = y0ñ - p1y
t1 = (y0ñ - p1y) / (p1vy - vy)
x1 = p1x + p1vx * t1
y1 = y0ñ + vy * t1
z1 = z0ñ + vz * t1

t2 = (y0ŋ - p2y) / (p2vy - vy)
x2 = p2x + p2vx * t2
y2 = y0ŋ + vy * t2
z2 = z0ŋ + vz * t2



print(x1,y1,z1,99,t1)
print(x2,y2,z2,99,t2)

dt = t2 - t1
print(dt)
