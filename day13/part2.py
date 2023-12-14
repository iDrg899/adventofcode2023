txt = [i.strip() for i in open('day13/input.txt').readlines()]
txt.append('')

patterns = []

i = 0
pattern = []
for i in txt:
    if i == '':
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(i)

ans = 0
for p in patterns:
    isReflectionPoint = False

    for r in range(1, len(p)):
        difference = 0
        for i in range(min(r, len(p) - r)):
            thing1 = p[r - i - 1]
            thing2 = p[r + i]
            for pos in range(len(thing1)):
                if thing1[pos] != thing2[pos]:
                    difference += 1
        if difference == 1:
            print('r =', r)
            ans += 100 * r
            break
    if difference == 1:
        continue
    
    ñ = [''.join([p[j][i] for j in range(len(p))]) for i in range(len(p[0]))]
    for c in range(1, len(ñ)):
        difference = 0
        for i in range(min(c, len(ñ) - c)):
            thing1 = ñ[c - i - 1]
            thing2 = ñ[c + i]
            for pos in range(len(thing1)):
                if thing1[pos] != thing2[pos]:
                    difference += 1
        if difference == 1:
            print('c =', c)
            ans += c
            break

print(ans)
