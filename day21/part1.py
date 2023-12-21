txt = [i.strip() for i in open('day21/input.txt').readlines()]

height = len(txt)
width = len(txt[0])

def step():
    global crustables
    
    uncrustables = []

    for point in crustables:
        row, col = point[0], point[1]
        
        for dirc in UDLR:
            rowChange, colChange = dirc[0], dirc[1]
            newPoint = (row + rowChange, col + colChange)
            if not (0 <= newPoint[0] < height and 0 <= newPoint[1] < width):
                continue
            if newPoint in uncrustables:
                continue
            if txt[newPoint[0]][newPoint[1]] in '.S':
                uncrustables.append(newPoint)
        
    crustables = uncrustables

start = (0, 0)
for lineIdx in range(len(txt)):
    line = txt[lineIdx]

    if 'S' in line:
        start = (lineIdx, line.index('S'))

crustables = [start]
UDLR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(64):
    step()
    print(len(crustables))
