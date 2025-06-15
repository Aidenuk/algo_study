#sliding window technique 


def minSubArrayLen(target, nums):
    left = 0
    sumN = 0
    result = float("inf")
    for i in range(len(nums)):
        sumN += nums[i]
        while sumN >= target:
            result = min(i - left + 1, result)
            sumN -= nums[left]
            left +=1 
        



    return 0 if result == float('inf') else result

# print(minSubArrayLen(7,[2,3,1,2,4,3]))
# print(minSubArrayLen(4,[1,4,4]))
# print(minSubArrayLen(11,[1,1,1,1,1,1,1,1]))
# print(minSubArrayLen(11,[1,2,3,4,5]))
print(minSubArrayLen(7,[2,3,1,2,4,3]))