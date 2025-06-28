# leetcode 1763
# Longest Nice Substring problem

# My Solution

def longestNiceSubstring(s):
    if len(s) < 2:
        return ""
    break_point = -1
    for i in range(len(s)):
        if s[i].isupper():
            if s[i].lower() not in s:
                break_point = i
                break
        elif s[i].islower():
            if s[i].upper() not in s:
                break_point = i
                break
        
    if break_point != -1:
        left_half = longestNiceSubstring(s[:break_point])
        right_half = longestNiceSubstring(s[break_point + 1:])
        if len(left_half) >= len(right_half):
            return left_half
        else:
            return right_half

    return s


# Better solution
def longestNiceSubstring(s):
    if len(s) < 2:
        return ""
    for i in range(len(s)):
        if (s[i].isupper() and s[i].lower() not in s) or (s[i].islower() and s[i].upper() not in s):
            left = longestNiceSubstring(s[:i])
            right = longestNiceSubstring(s[i+1:])
            return left if len(left) >= len(right) else right

    return s
