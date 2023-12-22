f = open("day02/input.txt")
txt = [i.strip() for i in f.readlines()]

_sum = 0

for line in txt:
    id, rounds = line.split(':')
    id = int(id.split()[1])
    rounds = [i.strip() for i in rounds.split(';')]

    possible = True
    for r in rounds:
        shows = [i.strip().split() for i in r.split(',')]
        for s in shows:
            num, color = int(s[0]), s[1]
            if color == 'red' and num > 12:
                possible = False
            if color == 'green' and num > 13:
                possible = False
            if color == 'blue' and num > 14:
                possible = False
    
    if possible:
        _sum += id
    
print(_sum)