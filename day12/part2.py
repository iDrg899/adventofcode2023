txt = [i.strip() for i in open('day12/input.txt').readlines()]

_sum = 0
for l in txt:
    print('line: ' + l)
    ways = 0

    syms, nums = l.split()
    syms = syms + '?' + syms + '?' + syms + '?' + syms + '?' + syms
    nums = nums + ',' + nums + ',' + nums + ',' + nums + ',' + nums
    nums = [int(thing) for thing in nums.split(',')]
    numbernums = len(nums)
    
    length = len(syms)
    working = length - sum(nums)

    broken, unknown = syms.count('#'), syms.count('?')
    possibleBrokens = syms.replace('?', '#') #        ##.####.##...#.#

    splitSyms = syms.split()

    possibilitiesLists = []
    for s in splitSyms: #??#?#
        possibilities = []

        for i in range(2**s.count('?')):
            key = bin(i)[2:]
            new = s
            for c in key:
                if c == '0':
                    new = new[:new.index('?')] + '.' + new[new.index('?') + 1:]
                else:
                    new = new[:new.index('?')] + '#' + new[new.index('?') + 1:]
            newer = [len(run) for run in new.split('.') if len(run) != 0]
            possibilities.append(newer)
            print(s, newer)
        possibilitiesLists.append(possibilities)

        # for i in range(2**len(s)):
        #     new = (bin(i)[2:]).replace('0', '.').replace('1', '#')
        #     for j in range(len(new)):
        #         good = True
        #         if new[j] == '.' and s[j] == '#':
        #             good = False
        #         if new[j] == '#' and s[j] == '.':
        #             good = False
        #         if good:
        #             # print(new)
        #             newer = [len(run) for run in new.split('.') if len(run) != 0]
        #             possibilities.append(newer)
        # possibilitiesLists.append(possibilities)
    
    print(possibilitiesLists)


    print(syms.split('.'))