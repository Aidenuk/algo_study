# Path sum problem: leet code
# my solution
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root != None and not root.right and not root.left:
            if root.val == targetSum: 
                return True
        # if targetSum == 0:
        #     return False
        if root == None:
            return False
            
        stack = [[root, root.val]]
        
        while stack:
            node, current_sum = stack.pop()
            if node == None:
                continue

            if node.left == None and node.right == None:
                # which means this is leaf node
                if current_sum == targetSum:
                    return True

            
            if node.right: stack.append((node.right, node.right.val + current_sum))
            if node.left: stack.append((node.left, node.left.val + current_sum))

        return False



#-------------------------------------------------------------------------------------------------------------------------------------------------------------



# has path sum: youtube solution
def hasPathSum(self, root, targetSum):
  if not root:
    return False
  
  stack = [(root, root.val)]
  while stack:
    curr, val = stack.pop()

    if not curr.left and not curr.right and val == targetSum:
      return True
    
    if curr.right:
      stack.append((curr.right, curr.right.val + val))
    if curr.left:
      stack.append((curr.left, curr.left.val + val))
  return False