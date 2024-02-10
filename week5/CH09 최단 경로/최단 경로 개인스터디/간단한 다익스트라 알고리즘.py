# 간단한 다익스트라 알고리즘 소스코드 - 노드의 총 개수가 5000개 이하일 경우
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미

# 노드의 개수, 간선의 개수 입력
n,m = map(int,input().split())
#시작 노드 입력받기
start = int(input())

# for _ in range(n+1)로 작성하여도 동일한 결과가 나옴
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크용 리스트
visited = [False] * (n+1)
#최단거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기

for _ in range(m):
    a, b, c = map(int, input().split())
    # a노드에서 b노드로 가는 가중치 c
    graph[a].append((b,c))

# 그래프 완성

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node(): # 완전 탐색 방식을 통한 가장 작은 가중치를 지닌 노드 찾기 
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:     # 방문하지 않은 상태이면서 이어져있는 노드 탐색
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:     #j는 도착노드와 가중치 2개의 value로 이루어져 있음
        distance[j[0]] = j[1]   # 현재 지점에서 갈 수 있는 노드에 값을 갱신해줌
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost    
                
# 다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])    