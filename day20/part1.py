txt = [i.strip() for i in open('day20/input.txt').readlines()]

destsOf = {}
typeOf = {}
stateOf = {}
memoryOf = {}

for l in txt:
    node, dests = l.split(' -> ')
    type, name = node[0], node[1:]
    typeOf[name] = type
    destsOf[name] = dests.split(', ')

    if type == '%':
        stateOf[name] = 0              # 0 is off, 1 is on
    if type == '&':
        memoryOf[name] = {}

for n in destsOf:
    for d in destsOf[n]:
        if d not in typeOf:
            typeOf[d] = "lol it's a useless node"
        if typeOf[d] == '&':
            memoryOf[d][n] = 0



def pushButton():
    lows, highs = 1, 0

    signals = []
    for d in destsOf['roadcaster']:
        signals.append(['roadcaster', 0, d])         # 0 is low, 1 is high
        lows += 1
    
    lastProcessed = -1
    while lastProcessed < len(signals) - 1:
        
        signal = signals[lastProcessed + 1]
        origin, strength, node = signal[0], signal[1], signal[2]

        if typeOf[node] == '%':
            if strength == 0:
                stateOf[node] = 1 - stateOf[node]
                if stateOf[node] == 0:
                    for d in destsOf[node]:
                        signals.append([node, 0, d])
                        lows += 1
                else:
                    for d in destsOf[node]:
                        signals.append([node, 1, d])
                        highs += 1
        
        if typeOf[node] == '&':
            memoryOf[node][origin] = strength

            if 0 not in [memoryOf[node][n] for n in memoryOf[node]]: # if all memory is high
                for d in destsOf[node]:
                    signals.append([node, 0, d])
                    lows += 1
            else:
                for d in destsOf[node]:
                    signals.append([node, 1, d])
                    highs += 1
        
        lastProcessed += 1
    
    # print(signals)
    return lows, highs


lows, highs = 0, 0
for i in range(1000):
    l, h = pushButton()
    lows += l
    highs += h

print(lows, highs)
print(lows * highs)