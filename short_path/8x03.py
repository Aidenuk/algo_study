
import heapq
from collections import defaultdict

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

# times = [[1,2,1]]
# n = 2
# k = 2

graph = defaultdict(list)

for i,(a,b,c) in enumerate(times):
  graph[a].append((b,c))


q = []
heapq.heappush(q,(0,k))

visited = defaultdict(int)

while q:
  dist, now = heapq.heappop(q)
  
  if now in visited:
    continue
  visited[now] = dist
  for neighbor,edge in graph[now]:
    
    new_time = edge + dist
    heapq.heappush(q,(new_time,neighbor))

if len(visited) == n:
  print(max(visited.values()))
print(-1)


# for i in range(1,n+1):
#   if distance[i] == INF:
#     print('inf')
#   else:
#     print(distance[i])


