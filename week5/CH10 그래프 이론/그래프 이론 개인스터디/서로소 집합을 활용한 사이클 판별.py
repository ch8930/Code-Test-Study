# 서로소 집합을 활용한 사이클 판별 소스코드

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
v, e = map(int, input().split())
parent = [i for i in range(v+1)]

cycle = False   # 사이클 발생 유무

for i in range(e):
    a ,b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):        
        cycle = True
        break
    
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent, a, b)
        
        
print("사이클 발생" if cycle else "사이클 발생하지 않음")        
        