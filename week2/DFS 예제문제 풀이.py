## 탐색 알고리즘 DFS/BFS

# 인접 행렬 방식 예제
'''
INF=99999999 # 무한의 비용 선언

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]

]

print(graph)
'''

# 인접 리스트 방식 예제
'''
graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)
'''

# DFS 예제

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end =' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)