txt = [i.strip() for i in open('day25/input.txt').readlines()]

INFINITY = 10000
START, END = 0, -3



connections = {}
distance = {}
paths = {}
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



# SNIP SNIP
connections['txl'].remove('hxq')
connections['hxq'].remove('txl')
connections['zcj'].remove('rtt')
connections['rtt'].remove('zcj')
connections['tpn'].remove('gxv')
connections['gxv'].remove('tpn')




for node in nodes:
    distance[node] = INFINITY
    paths[node] = []

distance[nodes[START]] = 0
paths[nodes[START]] = [[]]
crustables = [nodes[START]]
while len(crustables) > 0:
    node = crustables[0]

    for node2 in connections[node]:
        for path in paths[node]:
            if node2 not in path:
                paths[node2].append(path + [node])
        if distance[node2] == INFINITY:
            crustables.append(node2)
        if distance[node2] > distance[node] + 1: distance[node2] = distance[node] + 1

    crustables.remove(node)


things = []

paths[nodes[END]].sort()
for path in paths[nodes[END]]:
    print(path)
    for i in range(len(path) - 1):
        things.append((path[i], path[i + 1]))

count = 0
for node in nodes:
    if distance[node] == INFINITY:
        count += 1
print(count)

print(count * (len(nodes) - count))