
# leetcode 1137
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# T(k) = T(k - 3) + T(k - 2) + T(k - 1)

class Solution:
    def __init__(self):
        self.memo = {}


    def tribonacci(self, n: int):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        if n in self.memo:
            return self.memo[n]
        
        f = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        self.memo[n] = f
        return f


print(Solution().tribonacci(25))