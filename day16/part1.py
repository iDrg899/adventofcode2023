txt = [i.strip() for i in open('day16/sample.txt').readlines()]

beams = [[0, -1, [0, 1]]]
active = 1

done = False
# print(beams)

while not done:
    oldlen = len(beams)
    # print(oldlen)

    for bi in range(len(beams) - active, len(beams)):

        b = beams[bi]
        
        pos = [b[0] + b[2][0], b[1] + b[2][1]]

        if pos[0] < 0 or pos[0] > len(beams) or pos[1] < 0 or pos[1] > len(beams):
            continue
        char = txt[pos[0]][pos[1]]

        if char == '/':
            b[2] = [-b[2][1], -b[2][0]]
            if [pos[0], pos[1], b[2]] not in beams:
                beams.append([pos[0], pos[1], b[2]])
                active += 0
                # print('+--1')
        elif char == '\\':
            b[2] = [b[2][1], b[2][0]]
            if [pos[0], pos[1], b[2]] not in beams:
                beams.append([pos[0], pos[1], b[2]])
                active += 1
        elif char == '-':
            if b[2][1] == 0:
                b[2] = [0, -1]
                if [pos[0], pos[1], [0, 1]] not in beams:
                    beams.append([pos[0], pos[1], [0, 1]])
                    active += 1
                if [pos[0], pos[1], b[2]] not in beams:
                    beams.append([pos[0], pos[1], b[2]])
                    active += 1
        elif char == '|':
            if b[2][0] == 0:
                b[2] = [-1, 0]
                if [pos[0], pos[1], [1, 0]] not in beams:
                    beams.append([pos[0], pos[1], [1, 0]])
                    active += 1
                if [pos[0], pos[1], b[2]] not in beams:
                    beams.append([pos[0], pos[1], b[2]])
                    active += 1
        elif char == '.':
            if [pos[0], pos[1], b[2]] not in beams:
                beams.append([pos[0], pos[1], b[2]])
                active += 1

    if active == 0:
        done = True
    # print(beams, active)
    print(beams)



dumbList = []

for b in beams:
    if [b[0], b[1]] not in dumbList:
        dumbList.append([b[0], b[1]])

print(len(dumbList))