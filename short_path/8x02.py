
import sys

input = sys.stdin.readline

INF = int(1e9)

# a number of nodes
n = int(input())
#  a number of edges
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0


for i in range(m):
  a,b,c = map(int,input().split())
  graph[a][b] = c



for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] == INF:
      print("INF",end=" ")
    else:
      print(graph[i][j],end=" ")
  print()




