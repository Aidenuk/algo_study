# leetcode 139
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true

s = "aaaaaaa"
wordDict = ["aaaa", "aa", "a"]

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# First solution
def wordBreak(s, wordDict):
    for i in range(1, len(s) + 1):
        first = s[0 : i]
        if first in wordDict:
            remaining = s[i:]  
            if len(remaining) == 0:
                return True
            comparing_word = ""
            pointer = 0
            for j in range(len(remaining)):  
                comparing_word = remaining[pointer : j + 1]
                if comparing_word in wordDict:
                    comparing_word = "" 
                    pointer = j + 1
            if pointer == len(remaining):
                return True
    return False






# Second solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check = [0]
        visited = set()
        while check:
            pointer = check.pop(0)
            if pointer == len(s):
                return True
            if pointer in visited:
                continue
            visited.add(pointer)
            
            for i in range(pointer + 1, len(s) + 1):
                word = s[pointer : i]
                if word in wordDict:
                    check.append(i)

        return False
    















# Optimal solution: for reference
def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[len(s)]
    
                    
     


# wordBreak(s, wordDict)

wordBreak(s, wordDict)