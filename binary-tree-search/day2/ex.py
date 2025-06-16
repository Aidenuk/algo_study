
def findMin(nums) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid > left:
            left = mid + 1
        elif mid < left:
            left +=1
            right -=1
    return left
        
       

print(findMin([3,4,5,1,2]))