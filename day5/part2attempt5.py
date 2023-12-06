txt = [i.strip() for i in open('day5/input.txt').readlines()]

nums = [int(i) for i in txt[0][7:].split()]

seeds = []
for i in range(len(nums)//2):
    seeds.append([nums[2 * i], nums[2 * i] + nums[2 * i + 1] - 1])

print(seeds)

translist = []

idx = 3
while idx < len(txt) - 2:
    transformations = []
    while txt[idx] != '':
        target, source, run = [int(i) for i in txt[idx].split()]
        transformations.append([source, source + run - 1, target - source])
        idx += 1
    
    idx += 2
    
    translist.append(transformations)

#
# What's up buddies so basically this function is really really unnecessary and I'm pretty sure there's
# a way to write it a lot better but it just updates the seeds based on a list of uhhh mappings or
# whatever by first listing everything that happens (starts of seed ranges, ends of seed ranges, starts
# of transformation ranges, ends of transformation ranges) in order, then adding ranges of seeds to the
# updated list as it goes. ඞඞඞඞඞ
#

def transform(seeds, translist):
    events = []
    for s in seeds:
        events.append([s[0], ['ss']])
        events.append([s[1], ['se']])
    for t in translist:
        events.append([t[0], ['ts', t[2]]])
        events.append([t[1], ['te', t[2]]])
    events.sort()

    eventIdx = 0
    starts = 0
    dense = False
    offset = 0
    newSeeds = []
    while eventIdx < len(events):
        print(newSeeds)
        e = events[eventIdx]
        print(e)
        if e[1][0] == 'ss':
            starts += 1
            if starts == 1:
                # start the range
                rangeStart = e[0]
                dense = True
                pass
        elif e[1][0] == 'se':
            starts -= 1
            if starts == 0:
                # end the range
                newSeeds.append([rangeStart + offset, e[0] + offset])
                dense = False
                pass
        elif e[1][0] == 'ts':
            if dense and rangeStart != e[0]:
                # end the range
                newSeeds.append([rangeStart + offset, e[0] + offset])
                dense = False
                offset += e[1][1]
                # start the range
                rangeStart = e[0] + 1
                dense = True
            else:
                offset += e[1][1]
        elif e[1][0] == 'te':
            if dense and rangeStart != e[0]:
                # end the range
                newSeeds.append([rangeStart + offset, e[0] + offset])
                dense = False
                offset -= e[1][1]
                # start the range
                rangeStart = e[0] + 1
                dense = True
            else:
                offset -= e[1][1]
        
        eventIdx += 1

    return newSeeds

for l in translist:
    print('currently doing ' + str(l))
    seeds = transform(seeds, l)
    print('\t' + str(seeds))

print(min([s[0] for s in seeds]))