
# 백준 1068 (remove subtree)

def solve():

  n = int(input())
  parents = list(map(int,input().split()))
  del_node = int(input())


  children = [[]for _ in range(n)]

  for i in range(n):
    if parents[i] == -1:
      root = i
    else:
      children[parents[i]].append(i)

  
  def remove_node(node):
    for child in children[node]:
      remove_node(child)
    children[node] = []

  def count_leaf(node):
    if not children[node]:
      return 1
    
    count = 0
    for child in children[node]:
      count += count_leaf(child)
    return count
  
  if del_node == root:
    return 0
  
  parent_node = parents[del_node]
  children[parent_node].remove(del_node)

  remove_node(del_node)

  return count_leaf(root)

print(solve())

    



