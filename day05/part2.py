txt = [i.strip() for i in open('day05/input.txt').readlines()]

nums = [int(i) for i in txt[0][7:].split()]

seeds = []

for i in range(len(nums)//2):
    seeds.append([nums[2 * i], nums[2 * i] + nums[2 * i + 1] - 1])

idx = 3
while idx < len(txt) - 2:
    # print(seeds)
    newSeeds = []
    while txt[idx] != '':
        transformations = []
        targetStart, sourceStart, run = [int(i) for i in txt[idx].split()]
        transformations.append([targetStart, sourceStart, run])
        sourceEnd = sourceStart + run - 1
        targetEnd = targetStart + run - 1
        for i in range(len(seeds)):
            seedStart, seedEnd = seeds[i]

            if (seedStart >= sourceStart and seedStart <= sourceEnd):
                newSeedStart = targetStart - sourceStart + seedStart

                if (seedEnd >= sourceStart and seedEnd <= sourceEnd):
                    newSeedEnd = targetStart - sourceStart + seedEnd
                    newSeeds.append([newSeedStart, newSeedEnd])
                else:
                    newSeedEnd = seedEnd
                    newSeeds.append([newSeedStart, targetEnd])
                    newSeeds.append([sourceStart + 1, newSeedEnd])
            else: # if seed start is out of range:
                newSeedStart = seedStart

                if (seedEnd >= sourceStart and seedEnd <= sourceEnd):
                    newSeedEnd = targetStart - sourceStart + seedEnd
                    newSeeds.append([newSeedStart, sourceStart - 1])
                    newSeeds.append([targetStart, newSeedEnd])
                else:
                    newSeedEnd = seedEnd
                    if [newSeedStart, newSeedEnd] not in newSeeds:
                        newSeeds.append([newSeedStart, newSeedEnd])
        idx += 1
    idx += 2
    seeds = newSeeds
    newSeeds = []
    for i in range(len(seeds)):
        if seeds[i] not in newSeeds:
            newSeeds.append(seeds[i])
    seeds = newSeeds
    # print(seeds)

print(min([i[0] for i in seeds]))
print(min([i[1] for i in seeds]))