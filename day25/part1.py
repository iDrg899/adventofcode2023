txt = [i.strip() for i in open('day25/input.txt').readlines()]

connections = {}
nodes = []

for line in txt:
    de, to = line.split(': ')
    to = to.split(' ')
    if de not in nodes:
        nodes.append(de)
    for node in to:
        if node not in nodes:
            nodes.append(node)

        if de not in connections:
            connections[de] = []
        if node not in connections:
            connections[node] = []
        connections[de].append(node)
        connections[node].append(de)


for START in range(1458):
    explored = []
    lump1 = [nodes[START]]
    done1 = False
    crustables = [nodes[START]]

    lBadList = []
    while not done1:
        done1 = True
        for node in crustables:
            potentialFriends = []
            
            for node2 in connections[node]:
                if node2 not in lump1:
                    potentialFriends.append(node2)
        
            if len(potentialFriends) == 1:
                if potentialFriends[0] not in lBadList:
                    lBadList.append(potentialFriends[0])
                    # print('L', node, potentialFriends[0], len(lBadList))
            else:
                for p in potentialFriends:
                    done1 = False
                    lump1.append(p)
                    crustables.append(p)
                    explored.append(p)
                    if p in lBadList:
                        # print('recovery happens', len(lBadList))
                        lBadList.remove(p)
            crustables.remove(node)

    if len(lump1) < 1000:
        print(len(lump1))

# 498680 < ans