txt = [i.strip() for i in open('day16/input.txt').readlines()]

height = len(txt)
width = len(txt[0])

beams = [(0, 0, 0, 1)]
oldActive = [(0, 0, 0, 1)]
active = []

def tryAdd(b):
    # Add if new and within the rectangle
    global active
    global beams

    y, x = b[0], b[1]

    if b in active or b in beams:
        print('DUPLICATE')
        return
    if y < 0 or y > height - 1:
        return
    if x < 0 or x > width - 1:
        return
    active.append(b)

done = False
while not done:
    for b in oldActive:

        y, x, yvel, xvel = b[0], b[1], b[2], b[3]

        char = txt[y][x]

        if char == '.':
            tryAdd((y + yvel, x + xvel, yvel, xvel))
        elif char == '/':
            tryAdd((y - xvel, x - yvel, -xvel, -yvel))
        elif char == '\\':
            tryAdd((y + xvel, x + yvel, xvel, yvel))
        elif char == '-':
            if yvel == 0:
                tryAdd((y + yvel, x + xvel, yvel, xvel))
            else:
                tryAdd((y, x - 1, 0, -1))
                tryAdd((y, x + 1, 0, 1))
        elif char == '|':
            if xvel == 0:
                tryAdd((y + yvel, x + xvel, yvel, xvel))
            else:
                tryAdd((y - 1, x, -1, 0))
                tryAdd((y + 1, x, 1, 0))
        
    if len(active) == 0:
        done = True

    oldActive = active
    active = []
    beams += oldActive


dumbList = []
for b in beams:
    if (b[0], b[1]) not in dumbList:
        dumbList.append((b[0], b[1]))

print(len(dumbList))