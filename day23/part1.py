txt = [i.strip() for i in open('day23/input.txt').readlines()]

ontos = {}
endPath = ()

# Returns length of a path (including starting arrow), end state of path
def walkStartingFrom(startState):
    global endPath

    row, col, dirc = startState[0], startState[1], startState[2]
    length = 1
    done = False
    while not done:
        if row == len(txt) - 1:
            done = True
            endPath = (length, startState[0], startState[1])

        elif txt[row - 1][col] == '.' and dirc != 'D':
            row -= 1
            dirc = 'U'
            length += 1
        elif txt[row + 1][col] == '.' and dirc != 'U':
            row += 1
            dirc = 'D'
            length += 1
        elif txt[row][col - 1] == '.' and dirc != 'R':
            col -= 1
            dirc = 'L'
            length += 1
        elif txt[row][col + 1] == '.' and dirc != 'L':
            col += 1
            dirc = 'R'
            length += 1
        else:
            done = True
    endState = [row, col, dirc]
    return length, endState

def getNewStartsFrom(state):
    row, col, trash = state

    newStarts = []

    if row == len(txt) - 1:
        return newStarts

    if txt[row - 1][col] == '^':
        newStarts.append([row - 1, col, 'U'])
    if txt[row + 1][col] == 'v':
        newStarts.append([row + 1, col, 'D'])
    if txt[row][col - 1] == '<':
        newStarts.append([row, col - 1, 'L'])
    if txt[row][col + 1] == '>':
        newStarts.append([row, col + 1, 'R'])
    
    return newStarts
    
def gobble(state):
    length, endState = walkStartingFrom(state)
    ontos[(length, state[0], state[1])] = []
    newStarts = getNewStartsFrom(endState)
    for newStart in newStarts:
        newLength = gobble(newStart)
        ontos[(length, state[0], state[1])].append((newLength, newStart[0], newStart[1]))
    return length

pathChains = [[(gobble([0, 1, 'D']), 0, 1)]]

done = False
while not done:
    done = True

    newPathChains = []
    for pc in pathChains:
        if pc[-1] == endPath:
            newPathChains.append(pc)
            continue
        for nextPath in ontos[pc[-1]]:
            done = False
            newPathChains.append(pc + [nextPath])
            # print(newPathChains, '\n')
    pathChains = [p for p in newPathChains]

# print(pathChains)

pathChainLengths = [sum([path[0] for path in pathChain]) - 1 for pathChain in pathChains]
print(max(pathChainLengths))
