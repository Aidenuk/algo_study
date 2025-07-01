# leetcode 494
# time error


def findTargetSumWays(nums, target):
    count = 0
    stack = [(0, 0)]
    cache = {0: 0}

    while stack:
        index, total = stack.pop()
        if index == len(nums):
            if total == target:
                count += 1
        else:
            stack.append((index + 1, total + nums[index]))
            stack.append((index + 1, total - nums[index]))
            print(f'calculate:{stack}')

    return count

print(findTargetSumWays([1,1,1,1,1], 3))