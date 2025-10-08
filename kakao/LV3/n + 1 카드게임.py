def solution(coin, cards):
    answer = 0
    n = len(cards)
    sum_value = n + 1
    total_round = n // 3
    check = {}
    result = [[0 for _ in range(2)] for _ in range(total_round + 1)]
    remain = 0

    use_coin = 0
    for i, v in enumerate(cards):
        use_coin = 1 if i >= n // 3 else 0
        target = sum_value - v

        if target not in check:
            check[v] = i
            continue

        else:
            use_coin = use_coin + 1 if check[target] >= n // 3 else use_coin

        if use_coin == 0:
            remain += 1
        else:
            round = (i - n // 3) // 2 + 1
            result[round][0] += 1
            result[round][1] += use_coin

    dp = [[-1 for _ in range(coin + 1)] for _ in range(total_round + 1)]

    d, c = result[1]

    if remain > 0:
        dp[1][coin] = remain - 1

    if d == 2:
        if coin >= c:
            dp[1][coin - c] = remain + 1
        if coin >= (c // 2):
            dp[1][coin - (c // 2)] = remain

    elif d > 0 and coin >= c:
        dp[1][coin - c] = remain

    for r, (d, c) in enumerate(result[2:]):
        r = r + 2
        for i, v in enumerate(dp[r - 1]):

            if v == -1:
                continue

            if v > 0:
                dp[r][i] = v - 1

            if d == 2:
                if i >= c:
                    dp[r][i - c] = max(v + 1, dp[r][i - c])
                if i >= (c // 2):
                    dp[r][i - (c // 2)] = max(v, dp[r][i - (c // 2)])

            elif d == 1 and i >= c:
                dp[r][i - c] = max(v, dp[r][i - c])

    for r in dp[1:]:
        print(r)

    for r in range(len(dp) - 1, -1, -1):
        if any(v != -1 for v in dp[r]):
            answer = r
            break

    return answer + 1
