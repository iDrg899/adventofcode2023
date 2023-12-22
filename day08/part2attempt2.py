import math

txt = [i.strip() for i in open('day08/input.txt').readlines()]

directions = txt[0] * 100

dict = {}
for i in txt[2:]:
    dict[i[0:3]] = [i[7:10], i[12:15]]

poses = []

for i in dict:
    if i[2] == 'A':
        poses.append(i)

zlists = []

for pos in poses:
    count = 0
    zlist = []

    i = 0
    while len(zlist) < 1:
        pos = dict[pos][0 if directions[i % len(directions)] == 'L' else 1]
        count += 1
        if pos[2] == 'Z':
            zlist.append(count)
        i += 1
    zlists.append(zlist)

coincidence = [zl[0] for zl in zlists]

print(math.lcm(coincidence[0], coincidence[1], coincidence[2], coincidence[3], coincidence[4], coincidence[5]))

# 68337144929