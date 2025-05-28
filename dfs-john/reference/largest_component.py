graph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2]
}


def largestComponent(graph):
    visited = set()
    largestCount = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        if (size > largestCount):
            largestCount = size 

    return largestCount




def exploreSize(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)
    size = 1
    for neighbor in graph[current]:
        size += exploreSize(graph, neighbor, visited)

    return size



result = largestComponent(graph)
print(result)