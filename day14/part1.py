txt = [i.strip() for i in open('day14/input.txt').readlines()]

txt = [''.join([i[j] for i in txt]) for j in range(len(txt[0]))]

length = len(txt[0])

ans = 0
for l in txt:
    i = 0
    load = length
    print(l, i)
    while i < length:
        if l[i] == 'O':
            ans += load
            load -= 1
        if l[i] == '#':
            load = length - i - 1
        i += 1
print(ans)