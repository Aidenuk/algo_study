
#  BJ 12865 (0/1 Knapsack Problem)

import sys
input = sys.stdin.readline

# n = a number of bags / k = capacity of the bag
n,k = map(int,input().split())
# a new array which contains all the bag information
items = []

# allocate information of the bag along side with weight and value
for _ in range(n):
  weight,value = map(int,input().split())
  items.append((weight,value))

# initialise extra memery space in order to implement with tabulation DP
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
  weight,value = items[i-1]
  for w in range(1,k+1):
    if weight > w :
      # not to choose as the overweight
      dp[i][w] = dp[i-1][w]
    else:
      dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)

print(dp[n][k])


