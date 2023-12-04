f = open("input.txt")
txt = [i.strip() for i in f.readlines()]

score = 0

for line in txt:
    discard, info = line.split(':')
    winning, have = [i.strip().split() for i in info.split('|')]

    subscore = 0
    for num in winning:
        if num in have:
            if subscore == 0:
                subscore = 1
            else:
                subscore *= 2
    score += subscore

print(score)