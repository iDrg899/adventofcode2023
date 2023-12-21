txt = [i.strip() for i in open('day21/input.txt').readlines()]

gardens = 1 + sum([l.count('.') for l in txt])

bigBigShell = 92857
bigShell = 33496
smallShell = 3759

print(smallShell * 9 - bigShell)
print(smallShell * 25 - bigBigShell)

steps = 26501365
layers = steps // 131

# 6015798859 too low

layers = 2

print(layers)

fullSquares = (2 * layers + 1)**2 // 2
print(fullSquares)

if layers % 2 == 0:
    extra = 3759
else:
    extra = 3852 # uhhh

print(int(fullSquares / 2 * gardens + extra))