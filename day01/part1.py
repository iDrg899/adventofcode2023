f = open("day01/input.txt")
txt = [i.strip() for i in f.readlines()]

s = 0

for i in txt:

    for j in i:
        if j.isdigit():
            s += int(j)*10
            print(s)
            break
    for j in i:
        if j.isdigit():
            d = j
    s += int(d)
    print(s)

print(s)