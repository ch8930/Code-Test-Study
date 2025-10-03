def solution(survey, choices):
    answer = ''
    #     지표에 해당하는 성격 유형

    # 처음 코드
    # kakao_personality = {1: ('R', 'T'),
    #                      2: ('C', 'F'),
    #                      3: ('J', 'M'),
    #                      4: ('A', 'N')
    #                      }

    # 굳이 dictionary로 안해도 됨
    kakao_personality = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]

    personality_score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    # 처음 코드
    # for index, value in enumerate(survey):
    #     x = choices[index]
    #     if x < 4:
    #         personality_score[value[0]] += 4 - x
    #     elif x > 4:
    #         personality_score[value[1]] += x - 4

    # zip을 통해 개선
    for s, c in zip(survey, choices):
        if c < 4 :
            personality_score[s[0]] += 4 - c
        elif c > 4 :
            personality_score[s[1]] += c - 4

    for x in kakao_personality:
        first_score = personality_score[x[0]]
        second_score = personality_score[x[1]]

        # 처음 코드
        # if first_score > second_score:
        #     answer += x[0]
        # elif first_score < second_score:
        #     answer += x[1]
        # else:
        #     answer += x[0]

        answer += x[0] if first_score >= second_score else x[1]

    return answer