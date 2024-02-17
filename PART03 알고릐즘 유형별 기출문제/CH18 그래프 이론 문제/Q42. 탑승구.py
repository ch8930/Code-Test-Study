# Q42 - 탑승구

# 출입구 게이트 수
g = int(input())

gate = [0] * (g+1)

# 루트 노드 자기자신으로 초기화
for i in range(1, g+1):
    gate[i] = i
# 도킹할 비행기 수
p = int(input())

def find_parent(gate, x):
    if gate[x] != x:
        gate[x] = find_parent(gate, gate[x])
    return gate[x]

def union_parent(gate, x, y):
    x = find_parent(gate, x)
    y = find_parent(gate, y)
    if x < y:
        gate[y] = x
    else :
        gate[x] = y

result = 0

# 도킹할 수 있는 비행기 수찾기
for _ in range(p):
    data = find_parent(gate, int(input()))
    if data == 0:
        break
    union_parent(gate, data, data-1)
    result += 1
    
print(result)    
             
    