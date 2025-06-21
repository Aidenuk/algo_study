

# refer to solution below
def searchBST(root, val):
    while root:
        if root.val == val:
            return root
        elif root.val < val:
            root = root.right
        else:
            root = root.left
    return None




def searchBST(root, val):
    current_node = root
    while current_node:
        if current_node.val == val:
            return current_node
        elif current_node < val:
            current_node = current_node.right
        else:
            current_node = current_node.left
    return None