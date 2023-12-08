txt = [i.strip() for i in open('day7/input.txt').readlines()]

CARDS = '23456789TJQKA'
l = []

for line in txt:
    h = [0] * 13
    for i in range(len(CARDS)):
        h[i] = line[0:5].count(CARDS[i])
    bid = int(line[6:])
    h.sort()
    # print(h)
    if h[12] == 5:
        l.append([20, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
    elif h[12] == 4:
        l.append([19, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
    elif h[12] == 3:
        if h[11] == 2:
            l.append([18, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
        else:
            l.append([17, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
    elif h[12] == 2:
        if h[11] == 2:
            l.append([16, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
        else:
            l.append([15, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
    else:
        # print(i)
        # print(line[0:5])
        # l.append([max([CARDS.index(i) for i in line[0:5]]), CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
        l.append([14, CARDS.index(line[0]), CARDS.index(line[1]), CARDS.index(line[2]), CARDS.index(line[3]), CARDS.index(line[4]), bid])
        # print(max([CARDS.index(i) for i in line[0:5]]))

print(len(l))
l.sort()
# print(l)

ans = 0
for i in range(len(l)):
    print(i+1, int(l[i][6]))
    ans += (i + 1) * int(l[i][6])


# print(len(l))
print(ans)

#473238428
#253159128
#252441624