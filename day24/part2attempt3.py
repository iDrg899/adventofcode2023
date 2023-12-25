import math

txt = [i.strip() for i in open('day24/input.txt').readlines()]

points = []
for line in txt:
    pos, vel = line.split(' @ ')
    x, y, z = [int(i) for i in pos.split(', ')]
    xv, yv, zv = [int(i) for i in vel.split(', ')]
    points.append([[x, y, z], [xv, yv, zv]])


vx = 11
vy = -2

xToXñ = math.cos(math.atan(vx/vy))
yToXñ = math.sin(math.atan(vx/vy))

leftmost = 10000000000000000000000000
rightmost = -10000000000000000000000000

for pointIdx1 in range(len(points)):
    for pointIdx2 in range(pointIdx1 + 1, len(points)):
        p1 = points[pointIdx1]
        p1x, p1y, p1z = p1[0]
        p1vx, p1vy, p1vz = p1[1]
        p2 = points[pointIdx2]
        p2x, p2y, p2z = p2[0]
        p2vx, p2vy, p2vz = p2[1]


        # (p1x + p1vx*t, p1y + p1vy*t, p1z + p1vz*t)

        # ↓

        # ((p1x + p1vx*t) * xToXñ + (p1y + p1vy*t) * yToXñ, p1z + p1vz*t)
        # (p1x*xToXñ + p1y*yToXñ + (p1vx*xToXñ + p1vy*yToXñ)*t, p1z + p1vz*t)

        p1xñ = p1x*xToXñ + p1y*yToXñ
        p1vxñ = p1vx*xToXñ + p1vy*yToXñ
        p1yñ = p1z
        p1vyñ = p1vz

        p2xñ = p2x*xToXñ + p2y*yToXñ
        p2vxñ = p2vx*xToXñ + p2vy*yToXñ
        p2yñ = p2z
        p2vyñ = p2vz
        
        xñ = (p2yñ - p1yñ - (p2vyñ/p2vxñ)*p2xñ + (p1vyñ/p1vxñ)*p1xñ) / (p1vyñ/p1vxñ - p2vyñ/p2vxñ)

        if xñ < leftmost:
            leftmost = xñ
        if xñ > rightmost:
            rightmost = xñ

print(leftmost, rightmost)
print(rightmost - leftmost)