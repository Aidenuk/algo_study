
def lowestCommonAncestor(root, p, q):
    small = min(p.val, q.val)
    large = max(p.val, q.val)

    while root:
        if root.val > large:
            root = root.left
        elif root.val < small:
            root = root.right
        else:
            return root
    return None
