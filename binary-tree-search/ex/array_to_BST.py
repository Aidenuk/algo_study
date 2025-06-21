
#leetcode 108



from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left_index, right_index):
            if left_index > right_index:
                return None
                
            mid = (left_index + right_index) // 2
            node = TreeNode(nums[mid])
            
            node.left = helper(left_index, mid - 1)
            node.right = helper(mid + 1, right_index)
            
            return node

        return helper(0, len(nums) - 1)














# Helper function to print the tree (for testing)
def print_tree_inorder(root):
    if root:
        print_tree_inorder(root.left)
        print(root.val, end=" ")
        print_tree_inorder(root.right)

# Helper function to print the tree level by level (for testing)
def print_tree_levels(root):
    if not root:
        return
    
    queue = [root]
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            if node:
                print(node.val, end=" ")
                queue.append(node.left)
                queue.append(node.right)
            else:
                print("null", end=" ")
        print()

# Test function
def test_solution():
    sol = Solution()
    
    # Test case 1
    nums1 = [-10, -3, 0, 5, 9]
    result1 = sol.sortedArrayToBST(nums1)
    print("Test case 1:")
    print("Input:", nums1)
    print("Tree (inorder):", end=" ")
    print_tree_inorder(result1)
    print()
    
    # Test case 2
    nums2 = [1, 3]
    result2 = sol.sortedArrayToBST(nums2)
    print("Test case 2:")
    print("Input:", nums2)
    print("Tree (inorder):", end=" ")
    print_tree_inorder(result2)
    print()

if __name__ == "__main__":
    test_solution()