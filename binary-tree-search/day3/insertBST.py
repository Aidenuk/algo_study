

def insertIntoBST(root, val):
    new_node = TreeNode(val)

    if not root:
        return new_node
    current = root
    
    while True:
        if val < current.val:
           if current.left:
                current = current.left
           else:
            current.left = new_node
            break
        else:
            if current.right:
                current = current.right
            else:
                current.right = new_node
    return root