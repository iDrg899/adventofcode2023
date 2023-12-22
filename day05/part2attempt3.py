txt = [i.strip() for i in open('day05/input.txt').readlines()]

nums = [int(i) for i in txt[0][7:].split()]

seeds = []
for i in range(len(nums)//2):
    seeds.append([nums[2 * i], nums[2 * i] + nums[2 * i + 1] - 1])

print(seeds)

def transform(span, t):
    a, b = span[0], span[1]
    start = t[1]
    end = t[1] + t[2] - 1
    change = t[0] - t[1]
    new = []
    if a <= start:
        if b < start:
            new.append([a, b])
        elif b <= end:
            new.append([a, start - 1])
            new.append([start + change, b + change])
        else:
            new.append([a, start - 1])
            new.append([start + change, end + change])
            new.append([end + 1, b])
    elif a <= end:
        if b <= end:
            new.append([a + change, b + change])
        else:
            new.append([a + change, end + change])
            new.append([end + 1, b])
    else:
        new.append([a, b])
    return new

idx = 3
while idx < len(txt) - 2:
    newSeeds = seeds
    transformations = []
    while txt[idx] != '':
        target, source, run = [int(i) for i in txt[idx].split()]
        transformations.append([target, source, run])
        idx += 1

    for s in seeds:
        for t in transformations:
            s = transform(seeds[i], t)
            print(s)
        newSeeds += s
    
    idx += 2
    seeds = newSeeds

    newSeeds = []
    for i in seeds:
        if i not in newSeeds:
            newSeeds.append(i)
    seeds = newSeeds

    print(seeds)

print(min(seeds))