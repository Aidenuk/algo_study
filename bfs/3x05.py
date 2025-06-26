
# LeetCode 104
# Given the root of a binary tree, return its the maximum depth

from collections import deque

def dfs(root):
  stack = [(root,1)]
  max_depth = 0


  while stack:

    node,depth = stack.pop()
    max_depth = max(max_depth,depth)

    if node.left:
      stack.append(node.left,depth+1)
    
    if node.right:
      stack.append(node.right,depth+1)


  return max_depth
  
  

# 백준 2178

def solve():


  rows, cols = map(int,input().split())

  graph = []

  for i in range(rows):
    graph.append(list(map(int,input())))

  def bfs():
    q = deque([(0,0,1)])
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True


    while q:

      dx,dy,dist = q.popleft()
      if dx == rows-1 and dy == cols-1:
        return dist
      
      for new_x,new_y in [[-1,0],[1,0],[0,-1],[0,1]]:
        nx,ny = new_x + dx , new_y + dy

        if 0 <= nx < rows and 0 <= ny < cols and graph[nx][ny] == 1 and not visited[nx][ny]:
          visited[nx][ny] = True
          q.append((nx,ny,dist+1))
    return -1
  return bfs()
print(solve())