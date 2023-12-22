# As a note to anyone who may be looking at my solution for today:
# It's only been five minutes since I finished part two, but I already forgot what the code does.
# One thing I do remember is that part of the way I did part one was influenced by anticipating part two.
# That worked, I think, because I correctly guessed that I would need an easy way to record which symbol each part number corresponded to.
# Besides that, I don't want to think about anything else I did because it looks very messy.
# Nothing here is intended to be neat. That goes for all of my solutions. I kinda speedrun.

f = open("day03/input.txt")
txt = [i.strip() + '.' for i in f.readlines()]

parts = []

for lineIdx in range(len(txt)):
    line = txt[lineIdx]
    charIdx = 0
    while charIdx < len(line):
        char = line[charIdx]
        if char.isdigit():
            startIdx = charIdx
            partNumber = ''
            while line[charIdx].isdigit():
                partNumber += line[charIdx]
                charIdx += 1
            endIdx = charIdx
            # print(partNumber)


            for l in range(lineIdx - 1, lineIdx + 2):
                for c in range(startIdx - 1, endIdx + 1):
                    try:
                        if txt[l][c] == '*':
                            parts.append([1000*l + c, int(partNumber)])
                    except:
                        # print('not a gear')
                        pass


        charIdx += 1


gearsAlreadyDone = []

_sum = 0
for i in parts:
    if i[0] not in gearsAlreadyDone:
        nums = []
        for j in parts:
            if j[0] == i[0]:
                nums.append(j[1])
                print(nums)
        try:
            _sum += nums[0] * nums[1]
        except:
            pass
        gearsAlreadyDone.append(i[0])

print(_sum)