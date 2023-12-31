txt = [i.strip() for i in open('day21/input.txt').readlines()]

size = len(txt)

def step():
    global reachable, crustables, offReachable, offCrustables
    
    newCrustables = []
    
    temp = [i for i in reachable]
    reachable = [i for i in offReachable]
    offReachable = temp

    for point in crustables:
        row, col = point[0], point[1]
        
        for dirc in UDLR:
            rowChange, colChange = dirc[0], dirc[1]
            newPoint = (row + rowChange, col + colChange)
            if newPoint in offCrustables:
                continue
            if newPoint in reachable:
                continue
            if txt[newPoint[0] % size][newPoint[1] % size] in '.S':
                reachable.append(newPoint)
                newCrustables.append(newPoint)
    
    offCrustables = [i for i in crustables]
    crustables = [i for i in newCrustables]

start = (0, 0)
for lineIdx in range(len(txt)):
    line = txt[lineIdx]

    if 'S' in line:
        start = (lineIdx, line.index('S'))

reachable = [start]
crustables = [start]
offReachable = []
offCrustables = []

UDLR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 65 good
for i in range(327):
    step()

print(len(reachable))

dists = [abs(65 - c[0]) + abs(65 - c[1]) for c in crustables]
for d in dists:
    if d != dists[0]:
        print(d)
    else:
        print('.', end = '')

print('\n')

# reachable = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
# crustables = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
# offReachable = []
# offCrustables = []

# for i in range(65):
#     step()

# print(len(reachable))

# dists = [abs(-0.5 - c[0]) + abs(-0.5 - c[1]) for c in crustables]
# for d in dists:
#     if d != dists[0]:
#         print(d)
#     else:
#         print('.', end = '')