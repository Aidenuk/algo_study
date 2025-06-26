
nums = [1,1,2,3,5,8,13,21,34,55,89]

def fib(x):
  if x < 2:
    return x
  else:
    return fib(x-1) + fib(x-2)

# print(fib(5))

def dp_fibo(x):
  if x < 2:
    return x
  dp = [0,1]
  for i in range(2,x+1):
    dp.append(dp[i-1] + dp[i-2])
  return dp[x]

print(dp_fibo(10))

