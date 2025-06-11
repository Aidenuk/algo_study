#is same tree problem: leetcode
#my solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p,q]]
        while stack:
            first, second = stack.pop()
            if first == None and second == None:
                continue
            if first == None or second is None:
                return False
            if first.val != second.val:
                return False
            if first and second:
                stack.append([first.left, second.left])
                stack.append([first.right, second.right])
        return True
        


#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# same tree: youtube solution
def isSameTree(self, p, q):
  stack = [[p, q]]
  
  while stack:
    node1, node2 = stack.pop()

    if not node1 and not node2:
      continue
    elif None in [node1, node2] or node1.val != node2.val:
      return False
    
    stack.append([node1.right, node2.right])
    stack.append([node1.left, node1.left]) # does right first, left second order matter