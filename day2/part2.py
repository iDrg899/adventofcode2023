f = open("input.txt")
txt = [i.strip() for i in f.readlines()]

_sum = 0

for line in txt:
    id, rounds = line.split(':')
    id = int(id.split()[1])
    rounds = [i.strip() for i in rounds.split(';')]

    possible = True
    red = 0
    green = 0
    blue = 0
    for r in rounds:
        shows = [i.strip().split() for i in r.split(',')]
        for s in shows:
            num, color = int(s[0]), s[1]
            if color == 'red' and num > red:
                red = num
            if color == 'green' and num > green:
                green = num
            if color == 'blue' and num > blue:
                blue = num
    
    power = red * green * blue
    _sum += power
    
print(_sum)