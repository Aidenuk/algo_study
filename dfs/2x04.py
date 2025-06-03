# Leetcode PathSum 112
# first approach

def dfs(root,start):
  visited = set()
  stack =[start]
  target = 22
  res = 0 # the problem is that sum all the node value

  if start not in visited:
    visited.add(start)
  if root is None:
    print(False)
  
  while stack:
    node = stack.pop()
    res += node
    
    for neighbor in root[node]:
      if neighbor not in visited:
        stack.append(neighbor)
        if res == target:
          print(True)
  print(False)

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def tree_dfs(root):
  target = 22
  current_sum = 0
  if not root:
    print(False)

  stack = [(root,root.val)]

  while stack:
    node,sum = stack.pop()

    if not node.left and node.right:
      if sum == target:
        print(True)
    if node.right:
      stack.append((node.right, current_sum + sum))
    if node.left:
      stack.append((node.left, current_sum + sum))
  print(False)  

# The main reason the first apporach was wrong is that I should be able to understand between graph and tree
# Tree : there must be a root node along side with childeren nodes. Tree is not allowed to have a cycle, should be a number of N node = a number of edge N-1 otherwise, it is not tree.
# if edge < n-1 : not connected / edge = n-1 : Tree / edge > n-1 : cycle 

root = {
  5: [4,8],
  4:[5,11,None],
  8:[5,13,4],
  11:[4,7,2],
  13:[8,None,None],
  4:[8,None,1],
  7:[11],
  2:[2],
  1:[4]

}

dfs(root,5)
