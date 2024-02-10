# 실전 문제 2 - 팀 결성

n , m = map(int, input().split())

# 초기 설정 팀
team = [i for i in range(n+1)]

# 루트 노드 찾기
def check_root(team, x):
    if team[x] != x:
        team[x] = check_root(team, team[x])
    return team[x]    

# 팀 합치기 연산
def union_team(team, a, b):
    if team[a] == team[b]:
        return
    else:
        a = check_root(team, a)        
        b = check_root(team, b)
        
        if a < b:
            team[b] = a
        else :
            team[a] = b    

result = []

for _ in range(m):
    x, y, z = map(int, input().split())
    if x == 0:
        union_team(team, y, z)
    else:
        result.append('YES') if check_root(team,y) == check_root(team,z) else result.append('NO')   

for i in result:
    print(i)
       