# Leetcode 501

# my approach
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import Counter
        if not root:
            return []

        res = []
        
        def dfs(node):
            res.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        count = Counter(res)

        max_freq = max(count.values())

        result = []

        for num,freq in count.items():
            if freq == max_freq:
                result.append(num)
        return result


# Fastest solution
def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        c = Counter(res)
        freq = max(c.values(), default=0)
        return [x for x,y in c.items() if y == freq]