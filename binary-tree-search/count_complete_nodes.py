class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# root = [1,2,3,4,5,6]
def countNodes(rrr):
    left_left_most = 0
    right_left_most = 0
    def far_left(node, leftCount, rightLeftCount):
        while node.left or node.right:
            if node.left:
                leftCount += 1
            if node.right:
                new_node = node.right
                if new_node.left:
                    rightLeftCount += 1
    # far_left(rrr,left_left_most, right_left_most )
    def get_left_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth
    if left_left_most == right_left_most:
        if rrr:
            return (left_left_most ** 2) + countNodes(rrr.right)
    else:
        return (right_left_most ** 2) + countNodes(rrr.left)

    # left_left_most = get_left_depth(a.left)
    # right_left_most = get_left_depth(a.right)
    print(f'farleft and farright nodes are equal: {left_left_most } --- {right_left_most}')





countNodes(a)
