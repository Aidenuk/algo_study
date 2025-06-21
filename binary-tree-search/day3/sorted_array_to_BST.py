
# Slices - Recursive 

def sortedArrayToBST(self, num):
    if not num:
        return None
    
    mid = len(num) // 2 

    root = TreeNode(num[mid])
    root.left = self.sortedArrayToBST(num[:mid])
    root.right = self.sortedArrayToBST(num[mid+1:])

    return root


# Indices - Recursive 
# Time: O(n)
# Space: O(n)

def sortedArrayToBST(self, nums):
    def convert(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = convert(left, mid - 1)
        node.right = convert(mid + 1, right)
        return node
    return convert(0, len(nums) - 1)


# Iterative BFS
from collections import deque

def sortedArrayToBST(self, nums):
    if not nums:
        return None
    # Tree initialization
    n = len(nums)
    mid = n // 2 
    root = TreeNode(nums[mid])
    # Queue to keep track of parent, left and right
    # BFS initialization
    q = deque()
    q.append((root, 0, mid - 1))
    q.append((root, mid + 1, n - 1))

    while q:
        parent, left, right = q.popleft()
        if left <= right:
            mid = (left + right) // 2
            child = TreeNode(nums[mid])
            if nums[mid] < parent.val:
                parent.left = child
            else:
                parent.right = child
            q.append((child, left, mid - 1))
            q.append((child, mid + 1, right))
    return root