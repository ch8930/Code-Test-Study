# 기본적인 서로소 집합 알고리즘 소스코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
# find 함수의 경우 비효율적으로 작동함( 시간 복잡도가 높음)

# 경로 압축 기법을 사용한 find 함수, 부모 테이블에 루트 노드를 바로 넣어주기에 빠르게 찾을 수 있음
def find_parent2(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 find 함수에서의 가장 큰 차이는 재귀함수 호출 후 부모 테이블 값의 갱신 유무

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
parent = [0] * (v+1)

# 부모 테이블상에서, 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end =' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블:', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')                        