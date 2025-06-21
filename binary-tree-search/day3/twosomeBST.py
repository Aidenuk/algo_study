from collections import deque

def findTarget(root, k):
    queue = deque([root])
    num_set = ()

    while queue:
        node = queue.popleft()
        if (k - node.val) in num_set:
            return True
        else:
            num_set.add(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return False