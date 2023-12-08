txt = [i.strip() for i in open('day7/input.txt').readlines()]

CARDS = 'J23456789TQKA'
l = []

for line in txt:
    h = [0] * 13
    for i in range(len(CARDS)):
        h[i] = line[0:5].count(CARDS[i])
    h[0] = 0
    h.reverse()
    jangled = line[0:5].replace('J', CARDS[12 - h.index(max(h))])

    h.sort()
    print(h, end=' ')
    # print(line[0:5])
    # print(jangled)

    bid = int(line[6:])
    
    
    j = [0] * 13
    for i in range(len(CARDS)):
        j[i] = jangled.count(CARDS[i])
    j.sort()
    print(j)
    # print(h)
    if j[12] == 5:
        l.append([20, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
    elif j[12] == 4:
        l.append([19, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
    elif j[12] == 3:
        if j[11] == 2:
            l.append([18, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
        else:
            l.append([17, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
    elif j[12] == 2:
        if j[11] == 2:
            l.append([16, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
        else:
            l.append([15, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
    else:
        # print(i)
        # print(line[0:5])
        l.append([14, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
        # print(max([CARDS.index(i) for i in line[0:5]]))

# print(len(l))
l.sort()
# print(l)

ans = 0
for i in range(len(l)):
    # print(i+1, int(l[i][6]))
    ans += (i + 1) * int(l[i][6])


# print(len(l))
print(ans)
