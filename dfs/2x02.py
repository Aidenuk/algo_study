
# find a way to use stack
def stack_dfs(graph,start):
  visited = set()
  stack =[start]
  result = []

  while stack:
    node = stack.pop()

    if node not in visited:
      visited.add(node)
      result.append(node)


    
    for neighbor in reversed(graph[node]):
      if neighbor not in visited:
        stack.append(neighbor)

  print(result)

# find a way to use recursive
def recursive_dfs(graph,start):
  visited = set()
  def help_dfs(node):
    if node in visited:
      return
    visited.add(node)
    print(node,end=" ")

    for neighbor in graph[node]:
      if neighbor not in visited:
        help_dfs(neighbor)
  help_dfs(start)

# find a way to use lambda

def lambda_dfs(graph,start,visited):
  visited[start] = True
  print(start,end=" ")
  for neighbor in graph[start]:
    if not visited[neighbor]:
      lambda_dfs(graph,neighbor,visited)



  
graph = {
  0: [1,2],
  1: [0,3,4],
  2: [0,4,5],
  3: [1],
  4: [1,2],
  5: [2]
}
visited = {node : False for node in graph.keys()}


# stack_dfs(graph,0)
# recursive_dfs(graph,0)
lambda_dfs(graph,0,visited)