
#iterable dfs 

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

# def depthFirstPrint(graph, source):
#     stack = [ source ]

#     while(len(stack) > 0):
#         current = stack.pop()
#         print(f'source stack popped: {current}')
#         for neighbor in graph[current]:
#             stack.append(neighbor)



# depthFirstPrint(graph, "a")













#recursive dfs 
# def depthFirstPrint(graph, source):
#     print(f'recursive dfs: {source}')
#     for neighbor in graph[source]: 
#         depthFirstPrint(graph, neighbor)




# depthFirstPrint(graph, "a")


#Both functions above used stack


#Breadth first algorithm
#its only possible in a iterable way 



def breadthFirstPrint(graph, source):
    queue = [source]
    while (len(queue) > 0): 
        current = queue.pop(0)
        print(f'current queue shifted: {current}')
        for neighbor in graph[current]:
            queue.append(neighbor)



breadthFirstPrint(graph, "a")