txt = [i.strip() for i in open('day7/input.txt').readlines()]

CARDS = '23456789TJQKA'
l = []

for line in txt:
    hand, bid = line[0:5], int(line[6:])
    
    counts = []
    for c in CARDS:
        counts.append(hand.count(c))
    counts.sort()

    hand = hand.replace('T', 'a').replace('J', 'b').replace('Q', 'c').replace('K', 'd').replace('A', 'e')
    
    l.append([counts[12], counts[11], hand, bid])
    
l.sort()

ans = 0
for i in range(len(l)):
    ans += (i + 1) * int(l[i][3])

print(ans)