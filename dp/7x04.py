
# BJ 2579 계단 오르기

import sys
input = sys.stdin.readline

n = int(input())

stair = [int(input()) for _ in range(n)]

if n == 1:
  print(stair[0])
elif n == 2:
  print(stair[0] + stair[1])
else:
  dp = [0] * n
  dp[0] = stair[0]
  dp[1] = stair[0] + stair[1]
  dp[2] = max(dp[0]+dp[2], dp[1]+dp[2])

  for i in range(3, n):
    dp[i] = max(dp[i-2]+ stair[i], dp[i-3]+ stair[i-1] + stair[i])
  print(dp[n-1])


