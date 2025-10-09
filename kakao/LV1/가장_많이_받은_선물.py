def solution(friends, gifts):
    answer = 0
    index = {}
    # 준 선물
    gift_to = [0 for _ in range(len(friends))]
    # 받은 선물
    gift_from = [0 for _ in range(len(friends))]

    result = [0 for _ in range(len(friends))]

    for i, n in enumerate(friends):
        index[n] = i

    f_to_f = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for g in gifts:
        f, t = g.split()
        i_f = index[f]
        i_t = index[t]

        f_to_f[i_f][i_t] += 1

        gift_to[i_f] += 1
        gift_from[i_t] += 1

    gift_ratio = [t - f for t, f in zip(gift_to, gift_from)]


    for i, f_1 in enumerate(f_to_f):
        for j, f_2 in enumerate(f_1[i + 1:]):
            j += i + 1
            if f_to_f[i][j] > f_to_f[j][i]:
                result[i] += 1
            elif f_to_f[i][j] < f_to_f[j][i]:
                result[j] += 1
            else:
                if gift_ratio[i] > gift_ratio[j]:
                    result[i] += 1
                elif gift_ratio[i] < gift_ratio[j]:
                    result[j] += 1

    return max(result)