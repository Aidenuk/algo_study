
# Leetcode 215
# Later on we should be able to solve this problem by quick sort
import heapq

nums = [3,2,1,5,6,4]
k = 2

heap = []

for num in nums:
  heapq.heappush(heap,num)
  if len(heap) > k:
    heapq.heappop(heap)
print(heap[0])

  

# Leetcode 347
import heapq
from collections import Counter

count = Counter(nums)
heap = []
    
for num,freq in count.items():
  heapq.heappush(heap,(freq,num))
  if len(heap) > k:
    heapq.heappop(heap)
print([num for freq,num in heap])

# the fastest solution
counts = Counter(nums)
sorted_items_by_value = sorted(counts.items(), key=lambda item: item[1])[-k:]
result = []

for i in sorted_items_by_value:
  result.append(i[0])

print(result) 