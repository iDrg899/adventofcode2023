txt = [i.strip() for i in open('day12/input.txt').readlines()]

sumsToDict = {}
def sumsTo(num, terms):
    global sumsToDict
    if (num, terms) in sumsToDict:
        return sumsToDict[(num, terms)]
    
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
                # if terms == 1:
                #     print(new, s)

                if new not in ret:
                    ret.append(new)
    sumsToDict[(num, terms)] = ret
    return ret

_sum = 0
for li in range(len(txt)):
    print(li)
    l = txt[li]
    ways = 0

    syms, nums = l.split()
    syms = syms + '?' + syms + '?' + syms + '?' + syms + '?' + syms
    nums = nums + ',' + nums + ',' + nums + ',' + nums + ',' + nums
    nums = [int(thing) for thing in nums.split(',')]
    length = len(syms)
    numbernums = len(nums)
    working = length - sum(nums)
    
    broken, unknown = syms.count('#'), syms.count('?')
    possibleBrokens = syms.replace('?', '#') #        ##.####.##...#.#

    numToDistribute = working - numbernums + 1
    base = [0] + ([1] * (numbernums - 1)) + [0]


    # print(base, numToDistribute)

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

