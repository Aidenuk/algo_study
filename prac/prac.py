

def dfs(x,y):
  if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "0":
    return 
  if grid[x][y] == "0":
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
  



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


res = 0 
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == "1":
      dfs(i,j)
      res +=1

print(res)


def check_height(node):
  if not node:
    return 0
  
  left_height = check_height(node.left)
  if left_height == -1:
    return -1
  
  right_height = check_height(node.right)
  if right_height == -1:
    return -1
  
  if abs(left_height - right_height) > 1:
    return -1
  
  return 1 + max(left_height,right_height)
# return check_height(root) != -1

#     3
#    / \
#   9   20
#      /  \
#     15   7
# 실제 함수 호출 스택:
# check_height(3) 호출
# ├── check_height(9) 호출
# │   ├── check_height(None) → return 0
# │   ├── check_height(None) → return 0
# │   └── return 1 + max(0,0) = 1    ✅ 9 완료
# │
# ├── check_height(20) 호출  
# │   ├── check_height(15) 호출
# │   │   ├── check_height(None) → return 0
# │   │   ├── check_height(None) → return 0
# │   │   └── return 1 + max(0,0) = 1    ✅ 15 완료
# │   │
# │   ├── check_height(7) 호출
# │   │   ├── check_height(None) → return 0
# │   │   ├── check_height(None) → return 0
# │   │   └── return 1 + max(0,0) = 1    ✅ 7 완료
# │   │
# │   └── return 1 + max(1,1) = 2    ✅ 20 완료
# │
# └── return 1 + max(1,2) = 3    ✅ 3 완료


def recursive(root):
  if not root:
    return 0
  
  left_height = recursive(root.left)

  right_height = recursive(root.right)

  if left_height == -1:
    return -1
  if right_height == -1:
    return -1
  
  if abs(left_height - right_height) > 1:
    return -1
  return 1 + max(left_height,right_height)
# return recursive(root) != -1

