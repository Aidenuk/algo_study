# Reference from neetcode
# Leetcode 743

import collections

def networkDelayTime(times: List[List[int]], n:int, k:int):
    edges =  collections.defualtdict(list)
    for u, v, w in times:
        edges[u].append((v, w))
    
    minHeap = [(0, k)]
    visit = set()
    result = 0
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        result = max(result, w1)

        for n2, w2 in edges[n1]:
            if n2 not in visit:
                heap.heappush(minHeap, (w1 + w2, n2))