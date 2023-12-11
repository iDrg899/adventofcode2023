txt = [i.strip() for i in open('day11/input.txt').readlines()]

bigrows = []
bigcols = []

r = 0
while r < len(txt):
    if '#' not in txt[r]:
        # txt = txt[:r] + [('.' * len(txt[0]))] + txt[r:]
        # print('sus')
        # r += 1
        bigrows.append(r)
    r += 1

c = 0
while c < len(txt[0]):
    if '#' not in [l[c] for l in txt]:
        # for r in range(len(txt)):
        #     txt[r] = txt[r][:c] + '.' + txt[r][c:]
        # print('sus')
        bigcols.append(c)
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
        for num in range(min([gals[i][0], g[0]]), max([gals[i][0], g[0]])):
            if num in bigrows:
                _sum += 999999
        for num in range(min([gals[i][1], g[1]]), max([gals[i][1], g[1]])):
            if num in bigcols:
                _sum += 999999

print(_sum)