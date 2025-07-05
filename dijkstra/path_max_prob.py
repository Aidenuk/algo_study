# leetcode 1514
# timeout error


from typing import List
import collections

def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node:int) -> float:
    adj_list = collections.defaultdict(list)
    for i in range(len(edges)):
        adj_list[edges[i][0]].append((edges[i][1], succProb[i]))
        adj_list[edges[i][1]].append((edges[i][0], succProb[i]))
    
    result = [0.0] * n 
    result[start_node] = 0.0 # 1.0
    stack = [(start_node, 1.0)]
    while stack:
        curr_node , curr_prob = stack.pop()
        for neighbor, prob in adj_list[curr_node]:
                new_est = curr_prob * prob
                if new_est > result[neighbor]:
                    result[neighbor] = new_est
                    stack.append((neighbor, new_est))


    return result[end_node]


print(maxProbability(3, [[0,1],[1,2],[0,2]],[0.5,0.5,0.2], 0, 2))