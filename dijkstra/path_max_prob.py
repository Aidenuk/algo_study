# leetcode 1514
# timeout error


from typing import List
import collections
import heapq

def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node:int) -> float:
    adj_list = collections.defaultdict(list)
    for i in range(len(edges)):
        adj_list[edges[i][0]].append((edges[i][1], succProb[i]))
        adj_list[edges[i][1]].append((edges[i][0], succProb[i]))
    print(adj_list)
    result = [0.0] * n 
    result[start_node] = - 1.0 
    pq = [(-1.0, start_node)]
    visited = set()
    while pq:
        curr_prob , curr_node = heapq.heappop(pq) 
        curr_prob = - curr_prob
        if curr_node in visited:
            continue
        visited.add(curr_node)

        if curr_node == end_node:
             return curr_prob
        
        for neighbor, prob in adj_list[curr_node]:
                if neighbor not in visited:
                    new_est = curr_prob * prob
                    # result[neighbor] = new_est
                    heapq.heappush(pq, (-new_est, neighbor))
                    # pq.append((neighbor, new_est))

    return 0.0


print(maxProbability(3, [[0,1],[1,2],[0,2]],[0.5,0.5,0.2], 0, 2))