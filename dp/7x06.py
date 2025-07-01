
amount = 5
nums = [1,2,5]

def coins(nums,amount):

  dp =[0] * (amount +1)
  dp[0] =1
 
  for i in nums:
    for j in range(i, amount +1):
      dp[j] += dp[j-i]
 


# LT 494
nums = [1,1,1,1,1]
target = 3
def findTargetSumWays(nums,target):
        dp = {}

        def backtracking(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)] = (backtracking(i + 1, total + nums[i]) + backtracking(i+1,total-nums[i]))
            return dp[(i,total)]
        return backtracking(0,0)
findTargetSumWays(nums,target)
