# divide and conqeur 
# leetcode 169


from collections import Counter


def majorityElement(nums):
    newlist = dict(enumerate(nums))
    if not newlist:
        return None
    value_counts = Counter(newlist.values())
    return value_counts.most_common(1)[0][0]


print(majorityElement([3,2,3]))