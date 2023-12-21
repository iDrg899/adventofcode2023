txt = [i.strip() for i in open('day21/input.txt').readlines()]

height = len(txt)
width = len(txt[0])

def stepToOdd():
    # global evenCrustables
    # global oddReachable
    global oddCrustables

    oddCrustables = []
    
    for point in evenCrustables:
        row, col = point[0], point[1]
        
        for dirc in UDLR:
            rowChange, colChange = dirc[0], dirc[1]
            newPoint = (row + rowChange, col + colChange)
            if not (0 <= newPoint[0] < height and 0 <= newPoint[1] < width):
                continue
            if newPoint in oddReachable:
                continue
            if txt[newPoint[0]][newPoint[1]] in '.S':
                oddReachable.append(newPoint)
                oddCrustables.append(newPoint)

def stepToEven():
    # global oddCrustables
    # global evenReachable
    global evenCrustables
    
    evenCrustables = []

    for point in oddCrustables:
        row, col = point[0], point[1]
        
        for dirc in UDLR:
            rowChange, colChange = dirc[0], dirc[1]
            newPoint = (row + rowChange, col + colChange)
            if not (0 <= newPoint[0] < height and 0 <= newPoint[1] < width):
                continue
            if newPoint in evenReachable:
                continue
            if txt[newPoint[0]][newPoint[1]] in '.S':
                evenReachable.append(newPoint)
                evenCrustables.append(newPoint)

start = (0, 0)
for lineIdx in range(len(txt)):
    line = txt[lineIdx]

    if 'S' in line:
        start = (lineIdx, line.index('S'))

evenReachable = [start]
evenCrustables = [start]
oddReachable = []
oddCrustables = []

UDLR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(32):
    stepToOdd()
    stepToEven()
print(len(evenReachable))
print(len(oddReachable))
