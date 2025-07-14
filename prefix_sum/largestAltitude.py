# Leetcode 1732

def largestAltitude(gains):
    gains_sum = []
    current = 0
    gains_sum.append(current)
    for each_gain in gains:
        current += each_gain
        gains_sum.append(current)

    return max(gains_sum)





print(largestAltitude([-4,-3,-2,-1,4,3,2]))