# Q1 - 모험가 길드

# 사람수 입력 받음
n = int(input())

# 모험가의 공포도 입력받음
adv = list(map(int, input().split()))

# 오름차순 정렬 - 적은 난이도부터 묶어야 더 많은 그룹을 형성할 수 있음
adv.sort()

count = 0
result = 0


for i in adv:
    # for문이 돌때마다 모험가 한명씩 추가
    count += 1
    # 다음 사람의 공포도를 고려하여 묶는 방식
    if count >= i:
        # 하나의 그룹 완성
        result += 1
        # 새로운 그룹을 만들어야하므로 count 0으로 초기화
        count = 0               
        
print(result)        
