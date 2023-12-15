txt = [i.strip() for i in open('day15/input.txt').readlines()]
line = txt[0]

ans = 0
for i in line.split(','):
    cv = 0
    for c in i:    
        cv += ord(c)
        cv *= 17
        cv %= 256
    ans += cv

print(ans)