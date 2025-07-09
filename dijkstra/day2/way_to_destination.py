# leetcode 1976
# used bi-directional roads 

import collections
from typing import List
import heapq


def countPaths(n: int, roads: List[List[int]]) -> int:
    edges = collections.defaultdict(list)
    for u, v, w in roads:
        edges[u].append((v, w))
        edges[v].append((u, w))  
    minHeap = [(0, 0)]
    dist = [float('inf')] * n  
    count = [0] * n       
    dist[0] = 0
    count[0] = 1 
    while minHeap:
        d1, n1 = heapq.heappop(minHeap)
        if d1 > dist[n1]:
            continue
        for n2, d2 in edges[n1]:
          new_dist = d1 + d2
          if new_dist < dist[n2]:       
              dist[n2] = new_dist
              count[n2] = count[n1]   
              heapq.heappush(minHeap, (new_dist, n2))
          elif new_dist == dist[n2]:  
              count[n2] += count[n1]     

    return count[n-1]







print(countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))