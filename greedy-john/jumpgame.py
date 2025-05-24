

#shift the target if the value one before target is valid 
def canJump (nums) -> bool:
    target  = len(nums) -1
    for i in range(len(nums) -1, -1, -1):
        if  i + nums[i] >= target:
            target = i
    print(target)
    return True if target  == 0 else False 


result = canJump([1,1,0,4, 10])
print(result)