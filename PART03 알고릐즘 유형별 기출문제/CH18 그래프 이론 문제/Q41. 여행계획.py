# Q41 - 여행 계획
 
# 여행지의 수 방문할 도시의 수 입력받기
n, m = map(int, input().split())
parent = [0] * (n+1)

# 처음의 경우 자기자신이 부모로 초기화 중요!!!
for i in range(1,n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
for i in range (1, n+1):
    # i 노드와 연결된 여행지 입력받음
    data = list(map(int, input().split()))
    # i 노드와 j+1 여행지 연결해줌
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i, j+1)

# 여행 계획 입력받음
city = list(map(int, input().split()))

result = True

for i in range(m-1):
    if find_parent(parent, city[i]) != find_parent(parent, city[i+1]):
        result = False
        break 

print('YES' if result == True else 'NO')     