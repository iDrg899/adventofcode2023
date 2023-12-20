txt = [i.strip() for i in open('day17/input.txt').readlines()]
size = len(txt)

INFINITY = 5000

nodes = []
for r in range(size):
    row = []
    for i in range(size):
        row.append([INFINITY, INFINITY])
    nodes.append(row)

nodes[0][0] = [0, 0]
crustables = [(0, 0, 0), (0, 0, 1)]

lastRowChecked = -1

while len(crustables) > 0:
    rowIdx, nodeIdx, dircIdx = crustables[0]

    if rowIdx > lastRowChecked:
        lastRowChecked = rowIdx
        print(lastRowChecked)

    dist = nodes[rowIdx][nodeIdx][dircIdx]

    if dircIdx == 0: # if previous move was vertical
        for i in [-3, -2, -1, 1, 2, 3]:
            if 0 <= nodeIdx + i < size:
                if i > 0:
                    addlDist = sum([int(txt[rowIdx][nodeIdx + j]) for j in range(1, i + 1)])
                else:
                    addlDist = sum([int(txt[rowIdx][nodeIdx + j]) for j in range(i, 0)])
                if dist + addlDist < nodes[rowIdx][nodeIdx + i][1]:
                    nodes[rowIdx][nodeIdx + i][1] = dist + addlDist
                    crustables.append((rowIdx, nodeIdx + i, 1))
    else:
        for i in [-3, -2, -1, 1, 2, 3]:
            if 0 <= rowIdx + i < size:
                if i > 0:
                    addlDist = sum([int(txt[rowIdx + j][nodeIdx]) for j in range(1, i + 1)])
                else:
                    addlDist = sum([int(txt[rowIdx + j][nodeIdx]) for j in range(i, 0)])
                if dist + addlDist < nodes[rowIdx + i][nodeIdx][0]:
                    nodes[rowIdx + i][nodeIdx][0] = dist + addlDist
                    crustables.append((rowIdx + i, nodeIdx, 0))

    crustables.remove(crustables[0])

print(nodes[size - 1][size - 1])