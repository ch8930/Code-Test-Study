import heapq as h

def solution(alp, cop, problems):
    INF = 1e9
    state = []

    max_alp = -1
    max_cop = -1

    for p in problems:
        # 가장 높은 알고력과 코딩력
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])

    # alp, cop를 공부하는 방식도 problem의 타입에 맞게 추가해주면 dp 테이블 update 내부 로직이 단순해짐
    # problems += [[0,0,1,0,1], [0,0,0,1,1]]

    alp = max_alp if alp > max_alp else alp
    cop = max_cop if cop > max_cop else cop

    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]

    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):

            if i < max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)

            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            if i < max_alp or j < max_cop:
                for p in problems:

                    if i < p[0] or j < p[1]:
                        continue

                    next_alp = max_alp if (i + p[2]) > max_alp else i + p[2]
                    next_cop = max_cop if (j + p[3]) > max_cop else j + p[3]

                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + p[4])

            # problem으로 모두 정의 한 경우
            # if i < max_alp or j < max_cop :
            #     for p in problems :
            #         if i < p[0] or j < p[1] :
            #             continue
            #
            #         next_alp = max_alp if (i + p[2]) > max_alp else i + p[2]
            #         next_cop = max_cop if (j + p[3]) > max_cop else j + p[3]
            #
            #         dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + p[4])

    return dp[-1][-1]

# BFS 방식 -> 시간 초과
# def solution(alp, cop, problems):
#     INF = 1e9
#     state = []
#
#     max_alp = -1
#     max_cop = -1
#
#     for p in problems:
#         # 가장 높은 알고력과 코딩력
#         max_alp = max(max_alp, p[0])
#         max_cop = max(max_cop, p[1])
#
#     alp = max_alp if alp > max_alp else alp
#     cop = max_cop if cop > max_cop else cop
#
#     dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
#
#     dp[alp][cop] = 0
#
#     # 현재 상태 넣기
#     h.heappush(state, (0, alp, cop))
#
#     while state:
#
#         time, now_alp, now_cop = h.heappop(state)
#
#         if now_alp < max_alp:
#             if dp[now_alp + 1][now_cop] > time + 1:
#                 dp[now_alp + 1][now_cop] = time + 1
#                 if check_next_state(now_alp + 1, now_cop, max_alp, max_cop):
#                     h.heappush(state, (time + 1, now_alp + 1, now_cop))
#
#         if now_cop < max_cop:
#             if dp[now_alp][now_cop + 1] > time + 1:
#                 dp[now_alp][now_cop + 1] = time + 1
#                 if check_next_state(now_alp, now_cop + 1, max_alp, max_cop):
#                     h.heappush(state, (time + 1, now_alp, now_cop + 1))
#
#         if now_alp < max_alp or now_cop < max_cop:
#             for p in problems:
#                 # 문제를 해결할 알고력, 코딩력을 지니고 있지 못한 상태
#                 if now_alp < p[0] or now_cop < p[1]:
#                     continue
#
#                 next_alp = max_alp if (now_alp + p[2]) > max_alp else now_alp + p[2]
#                 next_cop = max_cop if (now_cop + p[3]) > max_cop else now_cop + p[3]
#
#                 if dp[next_alp][next_cop] > time + p[4]:
#                     dp[next_alp][next_cop] = time + p[4]
#
#                 if check_next_state(next_alp, next_cop, max_alp, max_cop):
#                     h.heappush(state, (time + p[4], next_alp, next_cop))
#
#     return dp[max_alp][max_cop]
#
# def check_next_state(alp, cop, max_alp, max_cop):
#     if alp < max_alp or cop < max_cop:
#         return True
#     return False