import math

txt = [i.strip() for i in open('day12/input.txt').readlines()]

_sum = 0

for l in txt:
    ways = 0

    syms, nums = l.split()
    # length = len(syms)
    nums = [int(thing) for thing in nums.split(',')]
    # numbernums = len(nums)
    # working = length - sum(nums)
    
    broken, unknown = syms.count('#'), syms.count('?')
    # possibleBrokens = syms.replace('?', '#') #        ##.####.##...#.#

    # print(sum(nums) - broken, unknown)
    print(math.comb(unknown, sum(nums) - broken))
    # if math.comb(unknown, sum(nums) - broken) > 10000:
    #     print(l)

    # starts = [0]
    # for n in nums[:-1]:
    #     starts.append(starts[-1] + n + 1)

    
    _sum += ways
print(_sum)

