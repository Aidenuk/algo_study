# https://www.geeksforgeeks.org/print-adjacency-list-for-a-directed-graph/
from collections import defaultdict


V = 3
# edges = [[0, 1], [1, 2], [2, 0]]
edges = [[0, 1], [1, 2], [1, 3], [2, 3], [3, 0]]

def printAdjList(edges, V):
    adj_list = defaultdict(list)
    for e in edges:
        a, b = e
        adj_list[a].append(b)

    for e in adj_list:
        print(f'res: {e} -> {adj_list[e]}')
        


printAdjList(edges, V)


# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# Breadth First Search or BFS for a Graph
def BFS(graph, i):
    queue = [i]
    visited = [False] * len(graph)
    result = []
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current)
        visited[current] = True

        for neighbor in graph[current]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                queue.append(neighbor)

    print(f"BFS Result: {result}")



BFS([[1,2], [0,2,3], [0,1,4], [1,4], [2,3]], 0)
