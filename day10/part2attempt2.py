txt = ['.' + i.strip() + '.' for i in open('day10/input.txt').readlines()]

for r in range(len(txt)):
    if 'S' in txt[r]:
        pos = [r, txt[r].index('S')]
print(pos)
count = 0

drawing = []
for l in txt:
    newLine = l.replace('|', ' █ ').replace('-', '   ').replace('F', '   ').replace('7', '   ').replace('L', ' █ ').replace('J', ' █ ').replace('.', '   ')
    drawing.append(newLine)
    newLine = l.replace('|', ' █ ').replace('-', '███').replace('F', ' ██').replace('7', '██ ').replace('L', ' ██').replace('J', '██ ').replace('.', ' O ')
    drawing.append(newLine)
    newLine = l.replace('|', ' █ ').replace('-', '   ').replace('F', ' █ ').replace('7', ' █ ').replace('L', '   ').replace('J', '   ').replace('.', '   ')
    drawing.append(newLine)

output = open('day10/output.txt', 'w', encoding='UTF8')
for i in drawing:
    output.write('\n' + i)