# 실전 문제3 - 도시 분할 계획 - 크루스칼 알고리즘을 통한 문제 해결

# 특정 원소가 속한 집함 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수와 간선(union 연산)의 개수 입력받기
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost, a, b)) 
    
# 간선 비용 오름차순 정렬
edges.sort()
last = 0
# 간선 하나씩 체크

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 앟는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
print(result)

print(result - last)   