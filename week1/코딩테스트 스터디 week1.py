
# 1이 될때까지 문제
'''
n, k = map(int, input().split())

while n >= k :
    if n % k != 0:
        n -= 1
        result += 1
    else :
        n /= k    
        result += 1

while n >= k :
    while n % k != 0 :
        n -= 1
        result += 1
    n /= k
    result += 1    

while n > 1:
    n -= 1
    result += 1


while True:
    num = (n // k) * k
'''    
# 상하좌우
'''
n = 5
input = 'LRRUD'

cd = [1, 1]

# 딕셔너리를 통한 매핑
mapping = {'L':(0, -1) , 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)}

for i in input:
    if i in mapping:
        dx = cd[0] + mapping[i][0]
        dy = cd[1] + mapping[i][1]
    if dx < 1 or dx > n or dy < 1 or dy > n :
        continue
    cd=[dx, dy]

print(cd[0], cd[1]) 
'''
# 시각 - 1초씩 늘려가면서 문자열 내에 3이 포함되어있는지 검사해서 1씩 증가시키기
'''
h = 5
result =0
for i in range(h+1):
    for j in range(60) :
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                result += 1
print(result)
'''

# 왕실의 나이트 - 입력받은 현재 위치를  
'''
input = 'f2'
result = 0
col = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


if input[0] in col :
    col_loc= col[input[0]]


for i in move:
    dx = col_loc + i[0]
    dy = int(input[1]) + i[1]

    print(dx, dy)

    if 1 <= dx <= 8 and 1 <= dy <= 8:
        result += 1

    else :
        continue

print(result)         
'''
# 게임 개발

size = [5, 5]
start = [1, 1, 0]
n = size[0]
m = size[1]
x = start[0]
y = start[1]
loc = start[2]
road = [[1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 0, 0, 0], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]
result = 0

road[x][y]=2

go = { 0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1) }

while True:
    count = 0
    for i in range(4):
        loc = (loc+3) % 4       # 왼쪽으로 회전
        count += 1
        if 0 <= x+go[loc][0] < n and 0 <= y+go[loc][1] < m :
            if road[x+go[loc][0]][y+go[loc][1]] == 0 :
                road[x+go[loc][0]][y+go[loc][1]] = 2
                x = x + go[loc][0]
                y = y + go[loc][1]
                print (x,y, loc)
                break
        else :
            continue
    if count == 4 :
        if road[x-go[loc][0]][y-go[loc][1]] == 2 :
            x = x - go[loc][0]
            y = y - go[loc][1]
            print(x, y, loc)
        else :
            break

result = sum(row.count(2) for row in road)

for row in road:
    for col in row:
        print(col, end=" ")
    print()    

print(result)    