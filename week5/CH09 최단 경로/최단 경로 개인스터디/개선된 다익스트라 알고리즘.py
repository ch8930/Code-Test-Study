# 개선된 다익스트라 알고리즘 - 최소 힙 방식을 사용
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n,m = map(int,input().split())
#시작 노드 입력받기
start = int(input())

# for _ in range(n+1)로 작성하여도 동일한 결과가 나옴
graph = [[] for i in range(n+1)]
#최단거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기

for _ in range(m):
    a, b, c = map(int, input().split())
    # a노드에서 b노드로 가는 가중치 c
    graph[a].append((b,c))
    
def dikjstra(start):
    q = []
    # 시작 노드로 가기 위한  최단 경로는 0으로 설정 후, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # q안에 데이터가 없을때까지 반복문 수행
        # 가장 최단 거리가 짧은 노드에 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:        # 이미 방문한 노드에는 최단거리가 저장되어 있음
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dikjstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i]) 