# Leetcode 1302
from collections import deque

def deepestLeavesSum(root):
  if not root:
    print(0)
  
  q = deque([root])
  while q:
    res = 0
    for _ in range(len(q)):
      node = q.popleft()
      res += node.val

      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    if not q:
      return res

def deepestLeaveStack(root):
  depth_sum = {}
  max_depth = 0

  stack = [(root,1)]

  while stack:
    node, depth =stack.pop()

    depth_sum[depth] = depth_sum.get(depth,0) + node.val
    max_depth = max(max_depth,depth)

    if node.left:
      stack.append((node.left, depth +1))
    if node.right:
      stack.append((node.right, depth+1))
  return depth_sum[max_depth]



