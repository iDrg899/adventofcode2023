txt = [i.strip() for i in open('day12/input.txt').readlines()]

def sumsTo(num, terms):
    if num == 0:
        return [[0] * terms]
    if terms == 0:
        return []
    ret = []
    for i in range(num, 0, -1):
        partial = sumsTo(num - i, terms - 1)
        for s in partial:
            for j in range(len(s) + 1):
                new = s[:j] + [i] + s[j:]

                # for debug
                if terms == 1:
                    print(new, s)

                if new not in ret:
                    ret.append(new)
    return ret

_sum = 0
for l in txt:
    ways = 0

    syms, nums = l.split()
    length = len(syms)
    nums = [int(thing) for thing in nums.split(',')]
    numbernums = len(nums)
    working = length - sum(nums)
    
    broken, unknown = syms.count('#'), syms.count('?')
    possibleBrokens = syms.replace('?', '#') #        ##.####.##...#.#

    numToDistribute = working - numbernums + 1
    base = [0] + ([1] * (numbernums - 1)) + [0]


    print(base, numToDistribute)

    for s in sumsTo(numToDistribute, numbernums + 1):
        list = [base[i] + s[i] for i in range(len(base))]
        string = '.' * list[0]
        for i in range(len(nums)):
            string += '#' * nums[i] + '.' * list[i + 1]

        good = True
        for i in range(len(string)):
            if string[i] == '.' and syms[i] == '#':
                good = False
            if string[i] == '#' and syms[i] == '.':
                good = False
        
        if good:
            ways += 1
        
    _sum += ways
print(_sum)

