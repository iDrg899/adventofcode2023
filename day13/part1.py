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
        if p[r - 1] == p[r]:
            isReflectionPoint = True
            for i in range(1, min(r, len(p) - r)):
                if p[r - i - 1] != p[r + i]:
                    isReflectionPoint = False
            if isReflectionPoint:
                print('r =', r)
                ans += 100 * r
                break
    if isReflectionPoint:
        continue
    
    ñ = [''.join([p[j][i] for j in range(len(p))]) for i in range(len(p[0]))]
    for c in range(1, len(ñ)):
        if ñ[c - 1] == ñ[c]:
            isReflectionPoint = True
            for i in range(1, min(c, len(ñ) - c)):
                if ñ[c - i - 1] != ñ[c + i]:
                    isReflectionPoint = False
            if isReflectionPoint:
                print('c =', c)
                ans += c
                break

print(ans)
