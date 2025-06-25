# leetcode 897

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def order(node):
            if not node:
                return
            order(node.left)
            node.left = None
            self.current.right = node
            self.current = node
            order(node.right)

        dummy = TreeNode(0)
        self.current = dummy
        order(root)
        return dummy.right