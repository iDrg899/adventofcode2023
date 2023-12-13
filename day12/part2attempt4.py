txt = [i.strip() for i in open('day12/input.txt').readlines()]

solved = {}

def solve(syms, nums, debug):
    global solved

    try:
        return solved[(syms, tuple(nums))]
    except:
        pass

    # print('    ' * debug + 'solving', syms, nums)

    ret = 0
    for i in range(len(syms) - nums[0] + 1):

        # Check if first chunk works
        good = True
        for j in range(nums[0]): # j = 0,1,2
            if syms[i + j] == '.':
                good = False
            if i > 0:
                if '#' in syms[:i]:
                    good = False
            if i + nums[0] < len(syms):
                if syms[i + nums[0]] == '#':
                    good = False
        if not good:
            continue

        # print('    ' * debug + 'good', i)

        # Do all remaining chunks
        if len(nums) == 1:
            if len(syms) > nums[0] + i + 1:
                if '#' not in syms[nums[0] + i + 1:]:
                    ret += 1
            else:
                ret += 1
        else:
            additional = solve(syms[nums[0] + i + 1:], nums[1:], debug + 1)
            if additional == 0:
                continue

            ret += additional

    # print('    ' * debug + str(ret))
    solved[(syms, tuple(nums))] = ret
    return ret
    

_sum = 0
for li in range(len(txt)):
    l = txt[li]
    print(li, end=': ')

    syms, nums = l.split()
    syms = syms + '?' + syms + '?' + syms + '?' + syms + '?' + syms
    nums = nums + ',' + nums + ',' + nums + ',' + nums + ',' + nums

    nums = [int(thing) for thing in nums.split(',')]

    ways = solve(syms, nums, 0)
    print(ways)
    _sum += ways
print('Answer:', _sum)
# 3933386801665 too high
# 3920510818506 too high
# 3920437278260

# 6
# 5
# 16
# 1
# 10