
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
  
  



