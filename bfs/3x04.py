from collections import deque
# 백준 1260 dfs,bfs


# def dfs(graph, start):
#     stack = [start]
#     visited = set()
#     result = []
    
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             result.append(node)
            
#             # 역순으로 추가 (작은 번호 우선)
#             for neighbor in reversed(graph[node]):
#                 if neighbor not in visited:
#                     stack.append(neighbor)
#     return result
def dfs(graph,start):
    visited = set([start])
    result =[start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor)
    return result


def dfs(graph,start):
    visited = set()
    result = []

    def dfs_helper(node):
        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)
    dfs_helper(start)
    return result
        




def bfs(graph, start):
    queue = deque([start])
    visited = set([start])  # 시작점 미리 방문 처리
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # 큐 추가시 방문 처리
                queue.append(neighbor)
    return result

# 입력 받기
n, m, v = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력 및 양방향 처리
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향!

# 정렬 (작은 번호 우선)
for i in range(1, n + 1):
    graph[i].sort()

# 실행 및 출력
dfs_result = dfs(graph, v)
bfs_result = bfs(graph, v)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))