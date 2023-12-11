txt = [i.strip() for i in open('day11/input.txt').readlines()]

r = 0
while r < len(txt):
    if '#' not in txt[r]:
        txt = txt[:r] + [('.' * len(txt[0]))] + txt[r:]
        r += 1
    r += 1

c = 0
while c < len(txt[0]):
    if '#' not in [l[c] for l in txt]:
        for r in range(len(txt)):
            txt[r] = txt[r][:c] + '.' + txt[r][c:]
        c += 1
    c += 1


gals = []
for r in range(len(txt)):
    for c in range(len(txt[r])):
        if txt[r][c] == '#':
            gals.append([r, c])

_sum = 0

for i in range(len(gals)):
    for g in gals[i + 1:]:
        _sum += abs(gals[i][0] - g[0]) + abs(gals[i][1] - g[1])

print(_sum)
