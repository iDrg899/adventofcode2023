txt = [i.strip() for i in open('day19/input.txt').readlines()]

workflows = {}

i = 0
while txt[i] != '':
    name, rules = txt[i][:-1].split('{')
    rules = rules.split(',')
    workflows[name] = rules

    i += 1

i += 1
parts = []
while i < len(txt):
    x, m, a, s = [int(i) for i in txt[i].replace('x', '').replace('m', '').replace('a', '').replace('s', '')[2:-1].split(',=')]
    parts.append([x, m, a, s])

    i += 1

accepted = []

for part in parts:
    x, m, a, s = part

    wf = 'in'

    done = False
    while not done:
        if wf == 'A':
            accepted.append(part)
            done = True
            break
        if wf == 'R':
            done = True
            break
        
        rules = workflows[wf]
        for r in rules:
            if ':' in r:
                cond, dest = r.split(':')
                if eval(cond):
                    wf = dest
                    break
            else:
                wf = r

print(accepted)
print(sum([sum([i for i in part]) for part in accepted]))