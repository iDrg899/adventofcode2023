txt = [i.strip() for i in open('day05/input.txt').readlines()]

seeds = [int(i) for i in txt[0][7:].split()]

print(seeds)

idx = 3
while idx < len(txt) - 2:
    newSeeds = [i for i in seeds]
    while txt[idx] != '':
        target, source, run = [int(i) for i in txt[idx].split()]
        for i in range(len(seeds)):
            s = seeds[i]
            if (s >= source and s < source + run):
                newSeeds[i] = target - source + s
        idx += 1
    idx += 2
    seeds = newSeeds
    print(seeds)

print(min(seeds))