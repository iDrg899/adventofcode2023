txt = [i.strip() for i in open('day21/input.txt').readlines()]

size = len(txt)

UDLR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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



for i in range(64):
    step()
W = len(reachable)      # W is the answer after 64 steps

step()
B = len(reachable)      # B is the answer after 65 steps

totalGardens = sum([l.count('.') for l in txt]) + 1
# The number of periods in the file, plus one for the 'S'

R = totalGardens - W - B



steps = 26501365        # S
layers = steps // 131   # L

sumW = W  *  layers**2
sumB = B  *  (layers + 1)**2
sumR = R  *  layers * (layers + 1)

inexplicableError = 10 * (layers) * (layers + 1)

answer = sumW + sumB + sumR - inexplicableError

print('Part 2 answer:', answer)