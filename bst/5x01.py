
# Leetcode 230

def stack(root,k):
  stack = []
  cur = root
  res = 0

  while stack or cur:
    while cur:
      stack.append(cur)
      cur = cur.left
    cur = stack.pop()
    res +=1
    if res == k:
      return cur.val
    cur = cur.right


# Leetcode 589

def preorder(root):
  stack = [root]
  res = []

  if not root:
    return []

  while stack:
    node = stack.pop()
    res.append(node.val)

    for item in reversed(node.children):
      res.append(item)
  return res


# 589 recursive way

def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        def dfs(node):
            res.append(node.val)
            for kid in node.children:
                dfs(kid)
        dfs(root)





