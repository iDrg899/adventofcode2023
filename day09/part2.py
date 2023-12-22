txt = [i.strip() for i in open('day09/input.txt').readlines()]

_sum = 0

for l in txt:
    nums = [int(i) for i in l.split()][::-1] # ←←← I would like to point out that these 6 characters are the only difference between the two parts

    depth = 0
    seqs = [nums]
    current = seqs[depth]

    while not all(n == 0 for n in current):
        seqs.append([current[i + 1] - current[i] for i in range(len(current) - 1)])
        depth += 1

        current = seqs[depth]

    subsum = sum([seq[-1] for seq in seqs])
    _sum += subsum
    
    for i in seqs:
        print(i)
    print(subsum)

print(_sum)
