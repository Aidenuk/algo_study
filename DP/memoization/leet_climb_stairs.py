

# climbx = climb(x-1) + climb(x-2)
# leetcode 70


memo = {}

def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo[n]
    f = climbStairs(n-1) + climbStairs(n-2)
    memo[n] = f
    return f


print(climbStairs(44))
    
    