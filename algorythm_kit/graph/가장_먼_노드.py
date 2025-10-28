from collections import deque

def solution(n, edge):
    INF = 1e9
    graph = [[] for _ in range(n + 1)]

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (n + 1)
    # 노드 1로부터의 거리 계산
    distance = [INF] * (n + 1)
    s = 1
    distance[s] = 0
    visited[s] = True
    q = deque()
    q.append(s)

    # 초기 값 넣어주기
    while q:

        now = q.popleft()

        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                distance[next] = distance[now] + 1
                q.append(next)

    print(distance)
    return distance[1:].count(max(distance[1:]))