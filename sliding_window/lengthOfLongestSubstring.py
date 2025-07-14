# leetcode 3 
# Initializing left and right at the initial index of string, keep moving right if the current letter
# is not in set, otherwise start removing character from starting right index of letter until there is duplicate anymore. 
# set longest to max length of current window when there is no duplicate

# Time complexity O(n)
# Space complexity O(n)


def longestSub(s):
  longest = 0
  substrings = set()
  left = 0
  right = 0

  while right < len(s):
    # window_coverage = (right - left) + 1
    if s[right] not in substrings:
        substrings.add(s[right])
        # if window_coverage > longest:
        #     longest = window_coverage
        longest = max(longest, right - left + 1)
        right +=1
    else:
        while s[right] in substrings:
            substrings.remove(s[left])
            left += 1
        substrings.add(s[right])
        right += 1
        


  return longest


# print(longestSub("abcabcbb"))
# print(longestSub("bbbbb"))
print(longestSub("pwwkew"))