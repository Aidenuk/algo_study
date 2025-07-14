# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
import collections

def containsNearbyDuplicate(nums, k):
    duplicates =[item for item, count in collections.Counter(nums).items() if count > 1]
    indices = []
    distances = []
    current = 0
    for item in duplicates:
        indices.append(nums.index(item))
    for e in indices:
        current += e
        distances.append(current)
    return distances


print(containsNearbyDuplicate([1,2,3,1,2,3], 2))