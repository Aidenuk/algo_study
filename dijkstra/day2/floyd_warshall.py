class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        INF = float('inf')
        
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        # create 0 distance for itself, ex: 1 to 1, 2 to 2
        print(dist)
        
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        print(dist)
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        min_reachable = n  
        result_city = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_reachable:
                min_reachable = count
                result_city = i
        
        return result_city


solution = Solution()
print(solution.findTheCity(
    4,
    [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],
    4
)) 
