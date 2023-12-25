import numpy

txt = [i.strip() for i in open('day24/input.txt').readlines()]

points = []
for line in txt:
    pos, vel = line.split(' @ ')
    x, y, z = [int(i) for i in pos.split(', ')]
    xv, yv, zv = [int(i) for i in vel.split(', ')]
    points.append([[x, y, z], [xv, yv, zv]])

vxRestrictions = []
vyRestrictions = []
vzRestrictions = []
# shortestDistance = 10**18 # Infinity
# closestPair = []
for pointIdx1 in range(len(points)):
    for pointIdx2 in range(pointIdx1 + 1, len(points)):
        p1 = points[pointIdx1]
        p1x, p1y, p1z = p1[0]
        p1vx, p1vy, p1vz = p1[1]
        p2 = points[pointIdx2]
        p2x, p2y, p2z = p2[0]
        p2vx, p2vy, p2vz = p2[1]

        if p1vx == p2vx:
            vxRestrictions.append([p1vx, p1x, p2x])
        if p1vy == p2vy:
            vyRestrictions.append([p1vy, p1y, p2y])
        if p1vz == p2vz:
            vzRestrictions.append([p1vz, p1z, p2z])
        
        # Distance between lines:
        # p1point = numpy.array(p1[0])
        # p1direction = numpy.array(p1[1])
        # p2point = numpy.array(p2[0])
        # p2direction = numpy.array(p2[1])

        # shortestDirection = numpy.cross(p1direction, p2direction)
        # someVector = p2point - p1point

        # shortestSegment = (numpy.dot(shortestDirection, someVector) / numpy.linalg.norm(someVector)**2) * someVector
        # distance = numpy.linalg.norm(shortestSegment)

        # if distance < shortestDistance:
        #     shortestDistance = distance
        #     closestPair = [p1, p2]

# print('Closest pair:', closestPair)

# (p2x - p1x) % (vx - p1vx) = 0

for xVel in range(-1000, 1):
    good = True
    for r in vxRestrictions:
        if xVel == r[0]:
            continue
        if (r[2] - r[1]) % (xVel - r[0]) != 0:
            good = False
    if good:
        print('good xVel:', xVel)
        vx = xVel
        
for yVel in range(1000):
    good = True
    for r in vyRestrictions:
        if yVel == r[0]:
            continue
        if (r[2] - r[1]) % (yVel - r[0]) != 0:
            good = False
    if good:
        print('good yVel:', yVel)
        vy = yVel

for zVel in range(1000):
    good = True
    for r in vzRestrictions:
        if zVel == r[0]:
            continue
        if (r[2] - r[1]) % (zVel - r[0]) != 0:
            good = False
    if good:
        print('good zVel:', zVel)
        vz = zVel

# vx, vy, vz = -3, 1, 2
# print('SETTING VELOCITY FOR SAMPLE')

# Note: I knew to check for vx < 0, vy > 0, vz > 0 and that x:y:z ≈ -11:2:3 from testing in 3D Desmos
# So the numbers I got (-330, 63, and 94) are probably correct

p1 = points[0]
p1x, p1y, p1z = p1[0]
p1vx, p1vy, p1vz = p1[1]
p2 = points[1]
p2x, p2y, p2z = p2[0]
p2vx, p2vy, p2vz = p2[1]

# p1vx*t - p2vx*s + vx*k = p2x - p1x
# p1vy*t - p2vy*s + vy*k = p2y - p1y
# p1vz*t - p2vz*s + vz*k = p2z - p1z
coeffs = numpy.array([[p1vx, -p2vx, vx],
                      [p1vy, -p2vy, vy],
                      [p1vz, -p2vz, vz]])
consts = numpy.array([p2x - p1x, p2y - p1y, p2z - p1z])
t, s, k = numpy.linalg.solve(coeffs, consts)

# I hope I interpreted the not-roundness right
t = round(t)
s = round(s)
k = round(k)

# For fun
print('t='+str(t))
print('s='+str(s))
print('k='+str(k))

p1collisionPoint = numpy.array([p1x + p1vx*t, p1y + p1vy*t, p1z + p1vz*t])
v = numpy.array([vx, vy, vz])

print(p1collisionPoint - t*v)
print(sum(p1collisionPoint - t*v))


# 985068525073823 too high
# 948485822969419