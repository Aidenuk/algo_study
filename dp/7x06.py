
amount = 5
nums = [1,2,5]

def coins(nums,amount):

  dp =[0] * (amount +1)
  dp[0] =1
 
  for i in nums:
    for j in range(i, amount +1):
      dp[j] += dp[j-i]
      
 






