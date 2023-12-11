# I got bored
# Enjoy golf

l = []
for c in [i.strip()for i in open("input.txt").readlines()]:
 w,h=[i.strip().split()for i in c.split(':')[1].split('|')];score=sum([n in h for n in w]);l.append(score)
q=[1]*len(l)
for c in range(len(l)):
 for i in range(c+1,c+l[c]+1):q[i]+=q[c]
print(sum([q[i]for i in range(len(l))]))
