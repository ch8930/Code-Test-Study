# Q11 - 뱀

from collections import deque

n = int(input())
k = int(input())
# 크기가 n인 정사각형 모양의 map 초기화
maps = [[0]*n for _ in range(n)]

# 사과의 위치 표기 사과가 있는 곳은 1임
for _ in range(k):
    x, y = map(int, input().split())
    maps[x-1][y-1] = 1
    
l = int(input())
check = deque()

# 뱀의 방향 전환 정보
for _ in range(l):
    a, b = input().split()
    check.append((int(a),b))

move = {1:(-1,0), 2:(0,1), 3:(1,0), 4:(0,-1)}

def turn_right(direction):
    direction += 1
    if direction == 5:
        direction = 1
    return direction
        
def turn_left(direction):
    direction -= 1
    if direction == 0:
        direction = 4
    return direction
# 뱀의 현재 정보 저장
q = deque()
# 뱀의 처음 위치저장
q.append((0,0))
direction = 2
time = 0

while True:
    # 방향 전환 check
    if check:
        t, d = check[0]
        if t == time:
            if d == 'L':
                direction = turn_left(direction)
            else :
                direction = turn_right(direction)
            # 방향을 바꿨으면 제거
            check.popleft()        
    
    # 현재 머리의 위치 가져오기
    hx, hy = q[0]
    
    # 방향에 맞게 머리 이동
    hx += move[direction][0]
    hy += move[direction][1]
    # 이동했으므로 1초 증가
    time += 1
    
    # 머리의 위치가 몸이랑 같이 있거나 벽에 다가간 경우
    if hx< 0 or hx >= n or hy < 0 or hy >= n or maps[hx][hy] == 2:
        break
    # 머리가 이동한 곳에 사과의 유무판단
    if maps[hx][hy] == 1:
        maps[hx][hy] = 2
    else:
        maps[hx][hy] = 2
        # 현재 꼬리 위치 정보
        tx, ty = q.pop()
        # 꼬리칸 비워줌
        maps[tx][ty] = 0
    # 머리위치 옮겨줌
    q.appendleft((hx,hy)) 
    
print(time)