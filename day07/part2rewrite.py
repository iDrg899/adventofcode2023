txt = [i.strip() for i in open('day7/input.txt').readlines()]

CARDS = 'J23456789TQKA'
l = []

for line in txt:
    hand, bid = line[0:5], int(line[6:])
    
    counts = []
    for c in CARDS:
        counts.append(hand.count(c))
    
    jacks = counts[0]
    counts[0] = 0
    counts.sort()
    counts[12] += jacks

    hand = hand.replace('J', '0').replace('T', 'a').replace('Q', 'c').replace('K', 'd').replace('A', 'e')
    
    l.append([counts[12], counts[11], hand, bid])
    
l.sort()

ans = 0
for i in range(len(l)):
    ans += (i + 1) * int(l[i][3])

print(ans)