from collections import deque, defaultdict
# root = [3,9,20,None,None,15,7]
# Definition for a binary tree node.
# my solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        queue = deque([[root, 0]])
        result = defaultdict(list)
        result[0].append(root.val)

        while queue:
            curr_node, level = queue.popleft()
            if not curr_node.left and not curr_node.right:
                continue
            
            if curr_node.left and curr_node.right:
                result[level + 1].append(curr_node.left.val)
                result[level + 1].append(curr_node.right.val)
            
            elif curr_node.left:
                result[level + 1].append(curr_node.left.val)

            else:
                result[level + 1].append(curr_node.right.val)
            
            if curr_node.left: queue.append([curr_node.left, level + 1])
            if curr_node.right: queue.append([curr_node.right, level + 1])
        return list(result.values())
    


#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# Level order problem solution
from collections import deque
# root = [3,9,20,None,None,15,7]

def levelOrder(self, root):
  if root == None:
    return []
  
  queue = deque([root])
  tree = [] #[[3], [9,20]... ]

  while queue:
    level = [] # [9,20]
    for i in range(len(queue)):
      node = queue.popleft()

      level.append(node.val) #[9,20...]

      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    tree.append(level)
  return tree




class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for e in matrix:
            if e[-1] < target:
                continue
            if e[-1] > target or e[-1] == target:
                left = 0 
                right = len(e) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if e[mid] == target:
                        return True
                    elif e[mid] < target:
                        left = mid + 1
                    else:
                        right = mid -1
        return False
        