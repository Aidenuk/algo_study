#shortest path problem
#breadth first approach could be better for finding solution to shortest path
#problem as dfs may go through everything and then find the right path in an unluck situation
#here it has linear complexity
from collections import deque


edges = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "v"],
    ["w", "v"],
]

#edge list -> adjecency list  
def edgeToGraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
        return graph


def shortestPath(edges, nodeA, nodeB):
    visited = set([nodeA])
    graph = edgeToGraph(edges)
    queue = deque([[nodeA, 0]])
    while(len(queue) > 0):
        node, distance = queue.popleft() 
        if node == nodeB: 
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])
    return -1

                




result = shortestPath(edges, "w", "x")
print(result)



