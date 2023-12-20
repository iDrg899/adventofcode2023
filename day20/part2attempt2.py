# bro there is a lot of failed code here that i didnt end up using or became messy so just ignore it

import math

txt = [i.strip() for i in open('day20/input.txt').readlines()]

destsOf = {}
typeOf = {}
stateOf = {}
memoryOf = {}

flipperList = []
conjList = []

for l in txt:
    node, dests = l.split(' -> ')
    type, name = node[0], node[1:]
    typeOf[name] = type
    destsOf[name] = dests.split(', ')

    if type == '%':
        stateOf[name] = 0              # 0 is off, 1 is on
        flipperList.append(name)
    if type == '&':
        memoryOf[name] = {}
        conjList.append(name)

for n in destsOf:
    for d in destsOf[n]:
        if d not in typeOf:
            typeOf[d] = "lol it's a useless node"
        if typeOf[d] == '&':
            memoryOf[d][n] = 0

mgOnesPositionLists = [[], [], [], []]

def pushButton(param):

    signals = []
    for d in destsOf['roadcaster']:
        signals.append(['roadcaster', 0, d])         # 0 is low, 1 is high
    
    mgSent = False

    lastProcessed = -1
    while lastProcessed < len(signals) - 1:
        
        signal = signals[lastProcessed + 1]
        origin, strength, node = signal[0], signal[1], signal[2]

        if node == 'rx' and strength == 0:
            return True

        if node == 'mg' and not mgSent:
            row = ''.join([str(memoryOf['mg'][n]) for n in memoryOf['mg']])
            if '1' in row:
                print(row.replace('0', ' '), param)
                mgSent = True
                
                mgOnesPositionLists[row.index('1')].append(param)
            if row.count('1') > 1:
                return

        if typeOf[node] == '%':
            if strength == 0:
                stateOf[node] = 1 - stateOf[node]
                if stateOf[node] == 0:
                    for d in destsOf[node]:
                        signals.append([node, 0, d])
                else:
                    for d in destsOf[node]:
                        signals.append([node, 1, d])
        
        if typeOf[node] == '&':
            memoryOf[node][origin] = strength

            if 0 not in [memoryOf[node][n] for n in memoryOf[node]]: # if all memory is high
                for d in destsOf[node]:
                    signals.append([node, 0, d])
            else:
                for d in destsOf[node]:
                    signals.append([node, 1, d])
        
        lastProcessed += 1
    
    # print(''.join(str(stateOf[n]) for n in flipperList).replace('0', ' '))

    # print(signals)
    return False

done = False
for i in range(10000):
    if pushButton(i):
        print('THE ANSWER IS', i)
        done = True
    
firsts = [l[0] for l in mgOnesPositionLists]
diffs = [l[1] - l[0] for l in mgOnesPositionLists]

print(firsts)
print(diffs)

print(math.lcm(diffs[0], diffs[1], diffs[2], diffs[3]))

# bro there is a lot of failed code here that i didnt end up using or became messy so just ignore it