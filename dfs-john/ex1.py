# Leetcode 1971 Find if Path Exists in a Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/



#depth first approach 
# n = 3
# edges = [[0,1],[1,2],[2,0]]
# source = 0
# destination = 2
from collections import defaultdict

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

def validPath(edges, source, dst, visited):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    
    if source == dst:
        return True
    
    if source in visited:
        return False
    visited.add(source)
    
    for neighbor in graph[source]:
        if validPath(edges, neighbor, dst, visited) == True:
            return True

    return False 


# result = validPath(edges, source, destination, set())
# print(result)


def validPathStack(edges, source, dst, visited):
    stack = [source]
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited.add(source)

    while(len(stack) > 0):
        current = stack.pop()
        if current  == dst: 
            return True
        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            stack.append(neighbor)
            visited.add(neighbor)
    return False


result = validPathStack(edges, source, destination, set())
print(result)