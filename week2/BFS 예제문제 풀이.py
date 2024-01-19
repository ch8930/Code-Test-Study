# BFS 예제
from collections import deque

def bfs(graph, start, visited):
    queue=deque([start])
    
    visited[start] = True       # 시작지점 방문

    while queue:        # 리스트 안에 데이터가 없으면 False 처리를 해준다.
        v = queue.popleft()     # 가장 작은 인덱스 방문
        print(v, end=' ')       # 방문한 노드 출력
        for i in  graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
graph = [       # 노드와 노드간 관계
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

visited = [False] * 9 # False 방문하지 않은 노드 True 방문한 노드

bfs(graph, 1, visited)      # BFS 탐색 시작지점
