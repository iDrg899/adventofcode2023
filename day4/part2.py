# Holy beans please do not look at the parts of this solution I didn't use what was i doing oh beans oh beans
# On second thought, don't look at it at all
# I almost rewrote the whole thing just so i could have something im proud of, but i cannot have pride in my life after creating this

f = open("input.txt")
txt = [i.strip() for i in f.readlines()]

score = 0

scores = {}
occurences = {}

# def runCard(cardNum):
#     global score
#     try:
#         subscore = scores[cardNum]
#         for i in range(subscore):
#             runCard(i + 1)
#         score += 1
#     except:
#         pass

for lineIdx in range(len(txt)):
    line = txt[lineIdx]

    cardNum, info = line.split(':')
    cardNum = int(cardNum.split()[1])
    
    winning, have = [i.strip().split() for i in info.split('|')]

    subscore = 0
    for num in winning:
        if num in have:
            subscore += 1

    scores[cardNum] = subscore

for card in range(1, len(txt) + 1):
    occurences[card] = 1

for card in range(1, len(txt) + 1):
    for i in range(scores[card]):
        occurences[card + i + 1] += occurences[card]

for card in range(1, len(txt) + 1):
    score += occurences[card]

print(score)
