# missing number 
#https://leetcode.com/problems/missing-number/?envType=problem-list-v2&envId=binary-search

def missingNumber(nums) -> int:
    indexes = []
    for i in range(len(nums) + 1):
        indexes.append(i)
    difference =  list(set(indexes)- set(nums))
    return difference[0]


print(missingNumber([0]))