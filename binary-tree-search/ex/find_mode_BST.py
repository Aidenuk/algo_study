
# Leetcode 501

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
 
        values = []
        def traverse(node):
            if not node:
                return
            values.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        freq = {}
        for val in values:
            freq[val] = freq.get(val, 0) + 1

        max_freq = max(freq.values())
        return [val for val, f in freq.items() if f == max_freq]