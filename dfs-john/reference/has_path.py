#depth first search / recursion

# graph = {
#     "f":["g", "i"],
#     "g": ["h"],
#     "h": [],
#     "i": ["g", "k"],
#     "j": ["i"],
#     "k": []
# }

# def hasPath(graph, src, dst):
#     if (src == dst):
#         return True
    
#     for neighbor in graph[src]:
#         if (hasPath(graph, neighbor, dst) == True):
#             return True
#     return False


# result = hasPath(graph, "f", "k")
# print(result)



#breadth first approach

# def hasPath(graph, src, dst):
#     queue = [src]

#     while(len(queue) > 0):
#         current = queue.pop(0)
#         if (current == dst):
#             return True
#         for neighbor in graph[current]:
#             queue.append(neighbor)


# result = hasPath(graph, "f", "k")
# print(result)



# if there is cycles in our graph, we should keep track of visited nodes, otherwise it goes to inifinate loop
# n = nodes
# e = edges
# Time: O(e)
# Space: O(n)
# below is depth first search method
edges = {
    "i": ["j", "k"],
    "j": ["i"],
    "k": ["i", "m", "l"],
    "m": ["k"],
    "l": ["k"],
    "o": ["n"],
    "n": ["o"]
}

def hasPath(graph, src, dst, visited):
    if (src == dst):
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
         if (hasPath(graph, neighbor, dst, visited) == True):
             return True
    return False



result = hasPath(edges, "j", "m", set())
print(result)

