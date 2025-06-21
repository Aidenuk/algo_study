
#leetcode 108



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






