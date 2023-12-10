txt = [i.strip() for i in open('day10/input.txt').readlines()]

for r in range(len(txt)):
    if 'S' in txt[r]:
        pos = [r, txt[r].index('S')]
print(pos)
count = 0
chain = []
chain.append(pos)

# cheat
pos[0] += 1
chain.append(pos)
count += 1
lastMove = 'D'


current = txt[pos[0]][pos[1]]
while current != 'S':
    if current == 'F':
        if lastMove == 'L':
            pos[0] += 1
            lastMove = 'D'
        elif lastMove == 'U':
            pos[1] += 1
            lastMove = 'R'
    
    elif current == '7':
        if lastMove == 'R':
            pos[0] += 1
            lastMove = 'D'
        elif lastMove == 'U':
            pos[1] -= 1
            lastMove = 'L'
    
    elif current == 'L':
        if lastMove == 'L':
            pos[0] -= 1
            lastMove = 'U'
        elif lastMove == 'D':
            pos[1] += 1
            lastMove = 'R'
    
    elif current == 'J':
        if lastMove == 'R':
            pos[0] -= 1
            lastMove = 'U'
        elif lastMove == 'D':
            pos[1] -= 1
            lastMove = 'L'
    
    elif current == '|':
        if lastMove == 'U':
            pos[0] -= 1
            lastMove = 'U'
        elif lastMove == 'D':
            pos[0] += 1
            lastMove = 'D'
    
    elif current == '-':
        if lastMove == 'L':
            pos[1] -= 1
            lastMove = 'L'
        elif lastMove == 'R':
            pos[1] += 1
            lastMove = 'R'

    # print(pos)
    chain.append([pos[0], pos[1]])
    
    # print(pos)    
    # print(current)

    count += 1
    
    current = txt[pos[0]][pos[1]]

drawing = []
for r in range(len(txt)):
    l = txt[r]
    for c in range(len(l)):
        if [r, c] not in chain:
            l = l[:c] + '.' + l[c + 1:]

    newLine = l.replace('|', ' █ ').replace('-', '   ').replace('F', '   ').replace('7', '   ').replace('L', ' █ ').replace('J', ' █ ').replace('.', '   ')
    drawing.append(newLine)
    newLine = l.replace('|', ' █ ').replace('-', '███').replace('F', ' ██').replace('7', '██ ').replace('L', ' ██').replace('J', '██ ').replace('.', ' O ')
    drawing.append(newLine)
    newLine = l.replace('|', ' █ ').replace('-', '   ').replace('F', ' █ ').replace('7', ' █ ').replace('L', '   ').replace('J', '   ').replace('.', '   ')
    drawing.append(newLine)

output = open('day10/output.txt', 'w', encoding='UTF8')
for i in drawing:
    output.write('\n' + i)
