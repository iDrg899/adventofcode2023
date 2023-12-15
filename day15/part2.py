txt = [i.strip() for i in open('day15/input.txt').readlines()]
line = txt[0]

def hash(s):
    ret = 0
    for c in s:    
        ret += ord(c)
        ret *= 17
        ret %= 256
    return ret

boxes = {}

for i in range(256):
    boxes[i] = []

for i in line.split(','):

    if '=' in i:
        label, length = i.split('=')
        length = int(length)

        pos = hash(label)

        found = False
        for b in range(len(boxes[pos])):
            if boxes[pos][b][0] == label:
                found = True
                boxes[pos][b] = (label, length)
                break
        
        if not found:
            boxes[pos].append((label, length))

    elif '-' in i:
        label = i.split('-')[0]
        pos = hash(label)
        boxes[pos] = [i for i in boxes[pos] if i[0] != label]

ans = 0
for i in boxes:
    subsum = 0
    for l in range(len(boxes[i])):
        print(boxes[i][l])
        subsum += (l + 1) * boxes[i][l][1]
    subsum *= (i + 1)
    ans += subsum

print(ans)
