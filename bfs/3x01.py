# deque 를 이용해서 최단거리 찾기

from collections import deque
n,m,k,x = map(int,input().split())
# 4,4,2,1
city = [[] for _ in range(n+1)]

# short_path = [[-1] for i in range(n+1)]
# short_path = {dis: [-1] for dis in range(n+1)}
short_path = [-1] * (n+1)
short_path[x] = 0
print(short_path)
for _ in range(m):
  i,j = map(int,input().split())
  city[i].append(j)


q = deque()

def bfs(x):

  q.append(x)
  while q:

    v = q.popleft()

    for i in city[v]:
      if short_path[i] == -1:
        short_path[i] = short_path[v] + 1
        q.append(i)


  find = False
  for i in range(1, len(short_path)):
    if short_path[i] == k:
      print(i)
      find = True
    if find == False:
      print(-1)

bfs(x)


graph = [
   [1,2],
   [0,3,4],
   [0,4,5],
   [1],
   [1,2],
   [2]
]

