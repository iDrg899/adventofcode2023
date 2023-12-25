import math

txt = [i.strip() for i in open('day24/input.txt').readlines()]

points = []
for line in txt:
    pos, vel = line.split(' @ ')
    x, y, z = [int(i) for i in pos.split(', ')]
    xv, yv, zv = [int(i) for i in vel.split(', ')]
    points.append([[x, y, z], [xv, yv, zv]])


count = 0
for pointIdx1 in range(len(points)):
    p1 = points[pointIdx1]
    p1x, p1y, p1z = p1[0]
    vel = p1[1]
    p1vx, p1vy, p1vz = vel

    # speed = math.sqrt(sum([i**2 for i in vel]))
    
    # print(str([i/speed+1 for i in vel])[1:-1].replace(' ', ''), end = ';')


    print('(' + str(p1x/1000000000000) + '+' + str(p1vx) + 't, ' + str(p1y/1000000000000) + '+' + str(p1vy) + 't, ' + str(p1z/1000000000000) + '+' + str(p1vz) + 't' + ')')
print()