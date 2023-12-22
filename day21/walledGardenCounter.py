txt = [i.strip() for i in open('day21/input.txt').readlines()]

count = 0
distancesFromStart = []

for rowIdx in range(1, len(txt) - 1):

    for colIdx in range(1, len(txt[0]) - 1):

        if txt[rowIdx][colIdx - 1: colIdx + 2] != '#.#':
            continue

        if txt[rowIdx - 1][colIdx] != '#':
            continue

        if txt[rowIdx + 1][colIdx] == '#':
            count += 1
            distancesFromStart.append(str(abs(65 - rowIdx) + abs(65 - colIdx)))

print('There are', count, 'walled garden plots.')
print('Distances from the walled garden plots to the start: ' + ', '.join(distancesFromStart))