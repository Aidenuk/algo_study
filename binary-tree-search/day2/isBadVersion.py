# First 

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res = -1
   
        for i in range(1, n + 1):
            if isBadVersion(i) == True:
                res = i
                break
        return res