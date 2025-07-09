

# let V = number of vertices in graph
# let dist = V * V array of minimum distances 
# for each vertex v
# 	dist[v][v] <- 0
# for each edge(u, v)
# 	dist[u][v] <= weight(u, v)
# for k from 1 to V
# 	for i from 1 to V
# 		for j from 1 to V
# 			if dist[i][j] > dist[i][k] + dist[k][j]
# 				dist[i][j] <- dist[i][k] + dist[k][j]
# 			end if


# leetcode 787


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k + 1):
            temp_dist = list(dist)
            for u, v, price in flights:
                if dist[u] != INF:
                    print(temp_dist[v])
                    temp_dist[v] = min(temp_dist[v], dist[u] + price)
            dist = temp_dist
        if dist[dst] != INF:
            return dist[dst]
        else:
            return -1
    
solution = Solution()
print(solution.findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1 ))