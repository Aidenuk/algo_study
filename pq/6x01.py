
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

  

