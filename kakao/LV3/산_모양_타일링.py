def solution(n, tops):
    dp = [0] * (2 * n + 1)
    dp[0] = 1

    if tops[0] == 1:
        dp[1] = 3
    else:
        dp[1] = 2

    for i in range(2, 2 * n + 1):

        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

        if i % 2 != 0 and tops[(i - 1) // 2] == 1:
            dp[i] = (dp[i] + dp[i - 1]) % 10007

    answer = dp[-1]

    return answer
