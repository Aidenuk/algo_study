class TreeNode:

    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
 
 
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

 
    def postorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)


    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True





tree = TreeNode(10)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(22)
tree.insert(11)
tree.insert(12)

# tree.postorder_traversal()
    

# print(tree.find(12))


# Delete Node in a BST
def deleteNode(self, root: Optional[TreeNode], key:int) -> Optional[TreeNode]:
    if not root:
        return root
    
    if key > root.val:
        root.right = self.deleteNode(root.right, key)
    elif key < root.val:
        root.left = self.deleteNode(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Find the min from right subtree
        cur = root.right
        while cur.left:
            cur = cur.left
        root.val = cur.val
        root.right = self.deleteNode(root.right, root.val)
    return root
