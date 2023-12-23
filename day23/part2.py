txt = [i.strip() for i in open('day23/input.txt').readlines()]

ontos = {}
endPath = ()

# Returns length of a path, end state of path
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
        newStarts.append([row - 2, col, 'U'])
    if txt[row + 1][col] == 'v':
        newStarts.append([row + 2, col, 'D'])
    if txt[row][col - 1] == '<':
        newStarts.append([row, col - 2, 'L'])
    if txt[row][col + 1] == '>':
        newStarts.append([row, col + 2, 'R'])
    
    return newStarts
    
def gobble(state):
    length, endState = walkStartingFrom(state)
    ontos[(length, state[0], state[1])] = []
    newStarts = getNewStartsFrom(endState)
    for newStart in newStarts:
        newLength = gobble(newStart)
        ontos[(length, state[0], state[1])].append((newLength, newStart[0], newStart[1]))
    return length

pathChains = [[((gobble([0, 1, 'D']), 0, 1), 'F')]]
# pathChains = [[((gobble([55, 53, 'D']), 55, 53), 'F')]]

_max = 0

# print(ontos)

done = False
while not done:
    print(len(pathChains), pathChains[-1][-1], _max)
    done = True

    newPathChains = []
    for pc in pathChains:
        if pc[-1][0] == endPath:
            if sum([path[0][0] for path in pc]) + len(pc) - 2 > _max:
                _max = sum([path[0][0] for path in pc]) + len(pc) - 2
            continue


        if pc[-1][0][0] == 1:   # If on a short path:
            for nextPath in ontos[pc[-1][0]]:
                if (nextPath, 'F') not in pc and (nextPath, 'B') not in pc:
                    done = False
                    newPathChains.append(pc + [(nextPath, 'F')])
            for potentialPath in ontos:
                if pc[-1][0] in ontos[potentialPath]:
                    if (potentialPath, 'F') not in pc and (potentialPath, 'B') not in pc:
                        done = False
                        newPathChains.append(pc + [(potentialPath, 'B')])



        elif pc[-1][1] == 'F':
            for nextPath in ontos[pc[-1][0]]:
                if (nextPath, 'F') not in pc and (nextPath, 'B') not in pc:
                    done = False
                    newPathChains.append(pc + [(nextPath, 'F')])


        else: # .... == 'B':
            for potentialPath in ontos:
                if pc[-1][0] in ontos[potentialPath]:
                    if (potentialPath, 'F') not in pc and (potentialPath, 'B') not in pc:
                        done = False
                        newPathChains.append(pc + [(potentialPath, 'B')])
    pathChains = [p for p in newPathChains]
    # print('\n'.join([str(i) for i in pathChains]))
    # input()

# print(pathChains)

# pathChainLengths = [sum([path[0][0] for path in pathChain]) + len(pathChain) - 2 for pathChain in pathChains]
# print(max(pathChainLengths))
print(_max)


# 6438 ≤ answer < 9475

# If I wait long enough, it will eventually print the answer.
# That's what I plan on doing.

# Update: It took many hours. I wish I had timed it.
