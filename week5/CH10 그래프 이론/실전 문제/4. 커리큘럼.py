# 실전 문제4 - 커리큘럼
from collections import deque
import copy

# 강의 수 입력 받기
n = int(input())

# 선이수 관계를 적용할 indegee 리스트와 그래프 초기화
indegree = [0]*(n+1)
time = [0]*(n+1)
graph = [[] for _ in range(n+1)]

# 커리큘럼 관계 반영
for i in range(1, n+1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    # 진입차수 값 할당해주는 코드
    indegree[i] = len(info[1:-1])
    for x in info[1:-1]:
        graph[x].append(i)

print(graph[1:])  
print(indegree[1:])  

def topology_sort():
    
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # 각 과목의 최소 시간 저장
    #result = [0] * (n+1)
    result = copy.deepcopy(time)
    
    while q:
        
        # 가장 첫번째 과목 출력
        now = q.popleft()
        
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now]+time[i])
            
            if indegree[i] == 0:
                q.append(i)
                
    for i in result[1:]:
        print(i)                
                    
topology_sort()            
            
              
    
    



