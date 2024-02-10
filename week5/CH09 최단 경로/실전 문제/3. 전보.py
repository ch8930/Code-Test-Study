# 실전 문제 3 - 전보
import heapq
import sys

INF = int(1e9)

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n+1)]
time = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a는 시작, b는 도착, c는 시간
    graph[a].append((b,c))
    
# 그래프 관계 완성

def transfer(start):
    q = []
    
    # 전달 시작
    heapq.heappush(q, (0, start))
    time[start] = 0 # 시작 지점은 0
    
    while q:
        t, now = heapq.heappop(q)
        
        if time[now] < t:   # 이미 방문한 노드임
            continue
        
        for i in graph[now]:
            check = time[now] + i[1]
            if time[i[0]] > check :
                time[i[0]] = check
                heapq.heappush(q,(check, i[0]))

print(graph)
transfer(k)
print(time)

city = 0
count = []

for i in time:
    if i == 0:
        continue
    if i != INF:
        city += 1
        #count.append(i)
        max_time = max(max_time, i) # 반복문을 수행하면서 값을 갱신해 주는 방법도 존재함
                       
#print(city, max(count))
print(city, max_time)               