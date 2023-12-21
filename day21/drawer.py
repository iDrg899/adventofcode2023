txt = [i.strip() * 3 for i in open('day21/input.txt').readlines() * 3]

size = len(txt)

def step():
    global reachable, crustables, offReachable, offCrustables
    
    offCrustables = [i for i in crustables]
    crustables = []
    
    temp = [i for i in reachable]
    reachable = [i for i in offReachable]
    offReachable = temp

    for point in offCrustables:
        row, col = point[0], point[1]
        
        for dirc in UDLR:
            rowChange, colChange = dirc[0], dirc[1]
            newPoint = (row + rowChange, col + colChange)
            if newPoint in reachable:
                continue
            if txt[newPoint[0] % size][newPoint[1] % size] in '.S':
                reachable.append(newPoint)
                crustables.append(newPoint)

start = (196, 196)

reachable = [start]
crustables = [start]
offReachable = []
offCrustables = []

UDLR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 65 good
for i in range(196):
    step()

print(len(reachable))

drawing = []

for r in range(size):
    l = ''
    for c in range(size):
        if (r, c) in reachable:
            l += 'O'
        else:
            l += txt[r][c]
    drawing.append(l)

output = open('day21/output.txt', 'w', encoding='UTF8')
for i in drawing:
    output.write('\n' + i)



# dists = [abs(65 - c[0]) + abs(65 - c[1]) for c in crustables]
# for d in dists:
#     if d != dists[0]:
#         print(d)
#     else:
#         print('.', end = '')

# print('\n')
