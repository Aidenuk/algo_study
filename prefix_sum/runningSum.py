# leetcode 1480


def runningSum(nums):
    prefix_sum = []
    current = 0
    for number in nums:
        current += number
        prefix_sum.append(current)

    return prefix_sum
        




print(runningSum([1,2,3,4]))
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]