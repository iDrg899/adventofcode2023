txt = [i.strip() for i in open('day8/input.txt').readlines()]

directions = txt[0] * 100

dict = {}
for i in txt[2:]:
    dict[i[0:3]] = [i[7:10], i[12:15]]

pos = 'AAA'
count = 0

for i in directions:
    pos = dict[pos][0 if i == 'L' else 1]
    count += 1
    if pos == 'ZZZ':
        break

print(count)