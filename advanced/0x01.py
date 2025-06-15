from collections import deque

def numIslands(grid):
  if not grid or not grid[0]:
    return 0
  rows, cols = len(grid), len(grid[0])

  visited = set()
  isIsland = 0

  def bfs(start_index):
    q = deque([start_index])
    visited.add(start_index)
    while q:
      index = q.popleft()
      row = index // cols
      col = index % cols

      for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        nr,nc = row + dr, col +dc


        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
          new_index = nr * cols + nc
          if new_index not in visited:
            visited.add(new_index)
            q.append(new_index)
  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == "1":
        index = row * cols + col
        if index not in visited:

          bfs(index)
          isIsland +=1
  return isIsland

        

grid = [
    ['1', '0', '1'],  # 첫 번째 행 (3개 열)
    ['1', '1', '0'],  # 두 번째 행 (3개 열)
    ['0', '0', '1']   # 세 번째 행 (3개 열)
]

print(numIslands(grid))

rows = len(grid)
cols = len(grid[0])

visited = set()
res = 0

def bfs(start_row,start_col):
  q = deque([start_row,start_col])

  visited.add(start_row * cols + start_col)
  while q:
    row,col = q.popleft()

    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nr,nc = row + dr, col + dc

      if 0 < nr <= rows and 0 < nc <= cols and grid[nr][nc] == "1":
        index = nr * cols + nc
        if index not in visited:
          visited.add(index)
          q.append(nr,nc)

  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == "1":
        index = row * cols + col
        if index not in visited:
          bfs(row,col)
          res +=1
  return res



def dfs(row,col):
  if 0 > row and rows >= row and 0 > col and cols >= col and grid[row][col] == "0":
    return 
  index = row * cols + col
  if index in visited:
    return
  visited.add(index)

  dfs(row-1,col)
  dfs(row+1,col)
  dfs(row,col-1)
  dfs(row,col+1)

  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == "1":
        index = row * cols + col
        if index not in visited:
          dfs(row,col)
          res +=1

  return res





#=======================================================================

start = 0
end = len(grid) * len(grid[0]) -1
visited = set()
isIsland = 0

# 1D -> 2D -> 1D using index

def bfs(start_index):
  q = deque([start_index])
  visited.add(start_index)

  while q:
    index = q.popleft()
    row = index // cols
    col = index % cols

    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nr,nc = row + dr, col + dc

      if 0 < nr <= rows and 0 < nc <= cols and grid[nr][nc] == "1":
        new_index = nr * cols + nc
        if new_index not in visited:
          visited.add(new_index)
          q.append(new_index)

for row in range(rows):
  for col in range(cols):
    if grid[row][col] == "1":
      index = row * cols + col
      if index not in visited:
        bfs(index)
        isIsland += 1


#=======================================================================

# 2D -> 1D


def bfs(start_row,start_col):
  q = deque([start_row,start_col])

  index = start_row * cols + start_col
  visited.add(index)

  while q:
    row,col = q.popleft()

    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nr,nc = row + dr, col+dc

      if 0 < nr <= rows and 0 < nc <= cols and grid[nr][nc] == "1":
        new_index = nr * cols + nc
        if new_index not in visited:
          visited.add(new_index)
          q.append((nr,nc))

  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == "1":
        index = row * cols + col
        if index not in visited:
          bfs(row,col)
          isIsland +=1
  return isIsland
        
#=======================================================================

# dfs with row,col

def dfs(row,col):
  if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
    return
  
  new_index = row * cols + col
  if new_index in visited:
    return
  visited.add(new_index)

  dfs(row-1,col)
  dfs(row+1,col)
  dfs(row,col+1)
  dfs(row,col-1)

  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == "1":
        index = row * cols + col
        if index not in visited:
          dfs(row,col)
          isIsland +=1

  return isIsland
  




grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]