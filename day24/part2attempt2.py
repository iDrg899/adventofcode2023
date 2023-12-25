# See https://en.wikipedia.org/wiki/Regulus_(geometry)
import numpy

def crossProduct(a, b):
    a1, a2, a3 = a
    b1, b2, b3 = b
    return [a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1]

txt = [i.strip() for i in open('day24/input.txt').readlines()]

points = []
for line in txt:
    pos, vel = line.split(' @ ')
    x, y, z = [int(i) for i in pos.split(', ')]
    xv, yv, zv = [int(i) for i in vel.split(', ')]
    points.append([[x, y, z], [xv, yv, zv]])

midpoints = []
for pointIdx1 in range(3):
    for pointIdx2 in range(pointIdx1 + 1, 3):
        p1 = points[pointIdx1]
        p1x, p1y, p1z = p1[0]
        p1v = p1[1]
        p1vx, p1vy, p1vz = p1v
        p2 = points[pointIdx2]
        p2x, p2y, p2z = p2[0]
        p2v = p2[1]
        p2vx, p2vy, p2vz = p2v

        # Find shortest segment between the two lines
        directionVector = crossProduct(p1v, p2v)
        vx, vy, vz = directionVector

        # (p1x + p1vx*t, p1y + p1vy*t, p1z + p1vz*t) + k*(vx, vy, vz) = (p2x + p2vx*s, p2y + p2vy*s, p2z + p2vz*s)
        # p1x + p1vx*t + vx*k = p2x + p2vx*s
        # p1vx*t - p2vx*s + vx*k = p2x - p1x
        # p1vy*t - p2vy*s + vy*k = p2y - p1y
        # p1vz*t - p2vz*s + vz*k = p2z - p1z
        coeffs = numpy.array([[p1vx, -p2vx, vx], [p1vy, -p2vy, vy], [p1vz, -p2vz, vz]])
        consts = numpy.array([p2x - p1x, p2y - p1y, p2z - p1z])

        try:
            t, s, k = numpy.linalg.solve(coeffs, consts)
        except:
            print('singular parallel')
            continue
        
        x = p1x + p1vx*t + vx*k/2
        y = p1y + p1vy*t + vy*k/2
        z = p1z + p1vz*t + vz*k/2

        midpoints.append([x, y, z])

m1 = numpy.array(midpoints[0])
m2 = numpy.array(midpoints[1])
m3 = numpy.array(midpoints[2])

normalVector = numpy.cross(m3-m1, m3-m2)
print(normalVector)
