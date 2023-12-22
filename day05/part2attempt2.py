txt = [i.strip() for i in open('day05/input.txt').readlines()]

def transform(rnge, transformations):
    a, b = rnge[0], rnge[1]
    clean = [[a, b]]
    dirty = []
    for t in transformations:
        start = t[1]
        end = t[1] + t[2] - 1
        change = t[1] - t[0]

        for c, d in clean:
            if c >= start and c <= end:
                if d >= start and d <= end:
                    dirty.append([c + change, d + change])
                else:
                    dirty.append([c + change, end + change])
                    dirty.append([end + 1, d])
            else:
                if d >= start and d <= end:
                    dirty.append([c, start - 1])
                    dirty.append([start + change, d + change])
                else:
                    dirty.append([c, d])
        clean = dirty
    return dirty

nums = [int(i) for i in txt[0][7:].split()]

seeds = []

for i in range(len(nums)//2):
    seeds.append([nums[2 * i], nums[2 * i] + nums[2 * i + 1] - 1])

idx = 3
while idx < len(txt) - 2:
    print(seeds)
    newSeeds = []
    transformations = []
    while txt[idx] != '':
        targetStart, sourceStart, run = [int(i) for i in txt[idx].split()]
        transformations.append([targetStart, sourceStart, run])
        idx += 1
    print('Hello' + str(transformations))

    for i in range(len(seeds)):
        seedStart, seedEnd = seeds[i]
        newSeeds += [i for i in transform([seedStart, seedEnd], transformations)]

    idx += 2
    seeds = newSeeds
    newSeeds = []
    for i in range(len(seeds)):
        if seeds[i] not in newSeeds:
            newSeeds.append(seeds[i])
    seeds = newSeeds

print(min([i[0] for i in seeds]))
print(min([i[1] for i in seeds]))