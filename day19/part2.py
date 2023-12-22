txt = [i.strip() for i in open('day19/input.txt').readlines()]

workflows = {}

i = 0
while txt[i] != '':
    name, rules = txt[i][:-1].split('{')
    rules = rules.split(',')
    workflows[name] = rules

    i += 1




def neg(s):
    # print(s)
    if '<' in s:
        a, b = s.split('<')
        return a + '>' + str(int(b) - 1)
    if '>' in s:
        a, b = s.split('>')
        return a + '<' + str(int(b) + 1)


accepted = []

paths = [[['in', 0, True]]] # If True, go to rule 0 of 'in'
newPaths = []

while len(paths) > 0:
    for path in paths:
        # print(path)
        wf, ruleIdx, trash = path[-1]

        rules = workflows[wf]
        rule = rules[ruleIdx]

        if ':' in rule:
            cond, dest = rule.split(':')
            newPaths.append(path + [[dest, 0, cond]])
            newPaths.append(path + [[wf, ruleIdx + 1, neg(cond)]])
        else:
            newPaths.append(path + [[rule, 0, True]])

    paths = []
    for path in newPaths:
        loc = path[-1][0]
        if loc == 'A':
            accepted.append(path)
        elif loc == 'R':
            pass
        else:
            paths.append(path)
    newPaths = []

_sum = 0

for path in accepted:
    # proper python ranges
    ranges = {'x':[1, 4001],
              'm':[1, 4001],
              'a':[1, 4001],
              's':[1, 4001]
              }

    conds = [i[2] for i in path]
    for c in conds:
        c = str(c)
        if c == 'True':
            continue
        elif '<' in c:
            ranges[c[0]][1] = int(c.split('<')[1])
        elif '>' in c:
            ranges[c[0]][0] = int(c.split('>')[1]) + 1
    
    prod = 1
    for i in 'xmas':
        prod *= (ranges[i][1] - ranges[i][0])

    _sum += prod

print(_sum)