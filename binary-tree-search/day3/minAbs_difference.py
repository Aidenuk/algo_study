

def getMinimumDifference(root):
    min_diff = float('inf')
    prev_val = float('-inf')
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            min_diff = min(min_diff, root.val - prev_val)
            prev_val = root.val
            root = root.right
    return min_diff