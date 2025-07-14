# leetcode 643 

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


def findMaxAverage(nums, k):
    left = 0 
    right = k
    max_avergage = float('-inf') # error when -1
    cur_sum = 0
    
    while right <= len(nums):
        cur_sum = sum(nums[left:right])
        max_avergage = max(max_avergage, cur_sum / k)
        left += 1
        right +=1
        
    return max_avergage


# print(findMaxAverage([1,12,-5,-6,50,3], 4))
print(findMaxAverage([5], 1))

# Above solution throws time limit exceeded error

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


def findMaxAverage(nums, k):
    left = 0 
    right = k
    max_avergage = float('-inf') # error when -1
    cur_sum = 0
    cur_sum = sum(nums[left:right])
    while right < len(nums) :
        cur_sum = cur_sum - nums[left]
        cur_sum = cur_sum + nums[right]
        max_avergage = max(max_avergage, cur_sum / k)
        right += 1
        left += 1

    return max_avergage
# print(findMaxAverage([1,12,-5,-6,50,3], 4))
# print(findMaxAverage([5], 1))
print(findMaxAverage([0,1,1,3,3], 4))

# Time complexity O(n)
# Space complexity O(1)

