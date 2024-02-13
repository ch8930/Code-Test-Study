# Q5 - 볼링공 고르기

# 볼링공 개수와 무게 입력 받음
n, m = map(int, input().split())

balls = list(map(int, input().split()))

result = 0
'''
for x in range(len(balls)):
    for y in range(len(balls)):
        if x != y and balls[x] != balls[y]:
            result += 1
        
if result % 2 == 0:
    result /= 2
else:
    result = result/2 + 1
    
print(int(result))
'''
# 답지 풀이

size = [0] * (n+1)

# 해당 사이즈의 공이 몇개 있는지 check
for i in balls:
    size[i] += 1

for i in size[1:]:
    c = i * (n-i)
    n -= i
    result += c
    
print(result)   
