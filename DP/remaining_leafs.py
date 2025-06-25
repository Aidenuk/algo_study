from collections import defaultdict

def countLeafNodesAfterRemoving(N, parents, to_delete):
    tree = defaultdict(list)
    root = -1

    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            tree[parent].append(child) 
        
    valid_nodes = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node == to_delete:
            pass
        else:
            valid_nodes.append(node)
            children = tree[node]
            for child in children:
                if child: queue.append(child)
    
    leafCount = 0
    for node in valid_nodes:
        children = tree[node]
        valid_child = any(child in valid_nodes for child in children)
        if not valid_child:
            leafCount += 1
    return leafCount



N = 5
parents = [-1, 0, 0, 1, 1]
delete = 2
print(countLeafNodesAfterRemoving(N, parents, delete)) 
#outcome:2
