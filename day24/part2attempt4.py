import numpy

txt = [i.strip() for i in open('day24/input.txt').readlines()]

points = []
for line in txt:
    pos, vel = line.split(' @ ')
    x, y, z = [int(i) for i in pos.split(', ')]
    xv, yv, zv = [int(i) for i in vel.split(', ')]
    points.append([[x, y, z], [xv, yv, zv]])


for t in [100000000000*i for i in range(96200, 96221)]:
    print('t =', t, end=': ')
    P = points[0]
    PPosition = numpy.array(P[0])
    PDirection = numpy.array(P[1])
    PPosition = PPosition + PDirection * t
    l2 = points[1]
    l2position = numpy.array(l2[0])
    l2direction = numpy.array(l2[1])
    l3 = points[2]
    l3position = numpy.array(l3[0])
    l3direction = numpy.array(l3[1])

    # Plane A from P and l2:
    ANormalVector = numpy.cross(l2position - PPosition, l2direction)
    # AD = numpy.dot(ANormalVector, PPosition)

    # Plane B from P and l2:
    BNormalVector = numpy.cross(l3position - PPosition, l3direction)
    # BD = numpy.dot(BNormalVector, PPosition)

    # Intersect A and B into line m
    mDirection = numpy.cross(ANormalVector//1000000000000000, BNormalVector//1000000000000000) # m: Point = P; Direction = mDirection

    # print(ANormalVector)
    # print(BNormalVector)
    # print(mDirection)



    # l4 = [[0, 0, 0], [0, 0, 1]]
    # mDirection = [1, 0, 0]
    # PPosition = [2, 2, 2]
    # Find distance between m and l4
    # It will be the projection of (a vector from a point on m to a point on l4) onto (mDirection cross l4direction)
    #                                                                          a onto v

    
    
    
    
    l4 = points[3]
    l4position = numpy.array(l4[0])
    l4direction = numpy.array(l4[1])

    a = l4position - PPosition
    v = numpy.cross(mDirection, l4direction)

    proj = (numpy.dot(a, v) / ((numpy.linalg.norm(v))**2)) * v

    print(numpy.linalg.norm(proj))
