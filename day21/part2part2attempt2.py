txt = [i.strip() for i in open('day21/input.txt').readlines()]

gardens = 1 + sum([l.count('.') for l in txt])

bigBigShell = 92857
bigShell = 33496
smallShell = 3759

d = 3759
o = 3646
pr = gardens - d - o


steps = 26501365
layers = steps // 131



ds = (layers + 1)**2
os = layers**2
prs = layers * (layers + 1)

print(ds, os, prs)
print(d, o, pr)

# 6015798859 too low

# ans: 606188414811259

print(d * ds + o * os + prs * pr
      - 10 * (layers) * (layers + 1))