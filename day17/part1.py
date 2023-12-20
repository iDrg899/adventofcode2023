txt = [i.strip() for i in open('day17/input.txt').readlines()]

INFINITY = 10000

size = len(txt)

nodes = []
for i in range(size):
    row = []
    for j in range(size):
        row.append([[[INFINITY, False], [INFINITY, False], [INFINITY, False]], [[INFINITY, False], [INFINITY, False], [INFINITY, False]], [[INFINITY, False], [INFINITY, False], [INFINITY, False]], [[INFINITY, False], [INFINITY, False], [INFINITY, False]]])
    nodes.append(row)

# nodes is a 141×141 array filled with 4×1 arrays

def minPath():
    done = True
    global nodes
    minPath = [0, 0, 0, 0]
    minDist = INFINITY
    for rowIdx in range(len(nodes)):
        row = nodes[rowIdx]
        for nodeIdx in range(len(row)):
            node = row[nodeIdx]
            for dircIdx in range(len(node)):
                dirc = node[dircIdx]
                for amtIdx in range(len(dirc)):
                    dist, searched = dirc[amtIdx]
                    if not searched:
                        done = False
                        if dist <= minDist:
                            minDist = dist
                            minPath = [rowIdx, nodeIdx, dircIdx, amtIdx]
    return minPath, done



nodes[0][0] = [[[0, False], [0, False], [0, False]], [[0, False], [0, False], [0, False]], [[0, False], [0, False], [0, False]], [[0, False], [0, False], [0, False]]]

numberOfTimesTheLastNodeHasBeenUpdated = 0
i = 0

lastRowChecked = -1
done = False
while not done:
# for j in range(1):
    path, done = minPath()
    rowIdx, nodeIdx, dircIdx, amtIdx = path

    # print(i, rowIdx, nodeIdx, dircIdx, amtIdx)
    # print(nodes[rowIdx][nodeIdx][dircIdx][amtIdx][1])

    if rowIdx > lastRowChecked:
        lastRowChecked = rowIdx
        print(lastRowChecked)
    
    # print(nodes[0][0])
    # print(nodes[0][1])
    # print('doing')

    dist = nodes[rowIdx][nodeIdx][dircIdx][amtIdx][0]
    amt = amtIdx + 1

    # each vel is [down, right, dircIdx]
    if dircIdx < 2: # if up or down
        vels = [[0, -3, 2], [0, -2, 2], [0, -1, 2], [0, 1, 3], [0, 2, 3], [0, 3, 3]]
    else:
        vels = [[-3, 0, 0], [-2, 0, 0], [-1, 0, 0], [1, 0, 1], [2, 0, 1], [3, 0, 1]]

    for v in vels:
        if rowIdx + v[0] == size - 1 and nodeIdx + v[1] == size - 1:
            numberOfTimesTheLastNodeHasBeenUpdated += 1
        if 0 <= rowIdx + v[0] < size and 0 <= nodeIdx + v[1] < size:
            newAmtIdx = abs(v[0]) + abs(v[1]) - 1
            addlDist = 0
            if newAmtIdx == 0:
                addlDist += int(txt[rowIdx + v[0]][nodeIdx + v[1]])
            elif newAmtIdx == 1:
                addlDist += int(txt[rowIdx + v[0] // 2][nodeIdx + v[1] // 2])
                addlDist += int(txt[rowIdx + v[0]][nodeIdx + v[1]])
            elif newAmtIdx == 2:
                addlDist += int(txt[rowIdx + v[0] // 3][nodeIdx + v[1] // 3])
                addlDist += int(txt[rowIdx + v[0] * 2 // 3][nodeIdx + v[1] * 2 // 3])
                addlDist += int(txt[rowIdx + v[0]][nodeIdx + v[1]])
            # print(rowIdx + v[0], nodeIdx + v[1])
            # print(nodes[rowIdx + v[0]][nodeIdx + v[1]][v[2]][newAmtIdx][0])
            nodes[rowIdx + v[0]][nodeIdx + v[1]][v[2]][newAmtIdx][0] = min(dist + addlDist, nodes[rowIdx + v[0]][nodeIdx + v[1]][v[2]][newAmtIdx][0])

    # print(nodes[0][0])
    nodes[rowIdx][nodeIdx][dircIdx][amtIdx][1] = True
    # print(nodes[0][0])
    # print(nodes[0][1])
    
    i += 1

print(nodes[size - 1][size - 1])