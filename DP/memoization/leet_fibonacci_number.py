# leetcode 509

# without memoization
regularComputationCount = 0
def regularFib (n): 
    global regularComputationCount 
    regularComputationCount +=1
    if n <= 1:
        return n
    print(f"function called {regularComputationCount} times.")
    return regularFib(n-2) + regularFib(n-1) 


print(regularFib(12))




# after memoization
class Solution:
    def __init__(self):
        self.memo = {}
        self.computationCount = 0

    def fib(self, n: int):
        if n == 0:
            return 0
        if n <= 1:
            return n
        if n in self.memo:
            print("Returned from memo")
            return self.memo[n]

        self.computationCount +=1
        f =  self.fib(n - 1) + self.fib(n - 2)
        print("Added to memo")
        self.memo[n] = f
        print(f"function called {self.computationCount} times.")
        return f



print(Solution().fib(4))





#Tabulation fibonacci
def fib(n:int): 
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i -2] + dp[i -1]
    return dp[n]

# Time: O(n)
# Space: O(n)


# fibonacci optimized solution
def fib(n): 
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev = 0
    cur = 1
    for i in range(2, n+ 1):
        prev, cur = cur, prev + 1
    return cur

# Time: O(n)
# Space: O(1)