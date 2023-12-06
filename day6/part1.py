times = [49, 97, 94, 94]
records = [263, 1532, 1378, 1851]

wayss = []

for i in range(4):
    time = times[i]
    record = records[i]
    ways = 0
    for t in range(time):
        distance = (time - t) * t
        if distance > record:
            ways += 1
    wayss.append(ways)


print(wayss[0] * wayss[1] * wayss[2] * wayss[3])