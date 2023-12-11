txt = [i.strip() for i in open('day8/input.txt').readlines()]

directions = txt[0]

dict = {}
for i in txt[2:]:
    dict[i[0:3]] = [i[7:10], i[12:15]]

pos = []
for i in dict:
    if i[2] == 'A':
        pos.append(i)

print(pos)

count = 0

i = 0
while True:
    done = True
    for j in range(len(pos)):
        pos[j] = dict[pos[j]][0 if directions[i % len(directions)] == 'L' else 1]
        if pos[j][2] != 'Z':
            done = False
    count += 1
    if done:
        break
    i += 1

print(pos)
print(count)

#26300