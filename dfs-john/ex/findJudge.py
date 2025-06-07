# https://leetcode.com/problems/find-the-town-judge/?envType=problem-list-v2&envId=graph



def findJudge(n, trust):
    trustScore = [0] * (n + 1)
    for a, b in trust:
        trustScore[a] -=1
        trustScore[b] +=1
    for i in range(1, n + 1):
        if trustScore[i] == n -1:
            return i
    return -1
    
print(findJudge(3, [[1,3], [2,3], [3,1]]))