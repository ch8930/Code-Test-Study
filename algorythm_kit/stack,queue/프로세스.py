from collections import deque


def solution(priorities, location):
    answer = 1
    os = deque((p, i == location) for i, p in enumerate(priorities))
    print(os)

    while os:

        process, loc = os.popleft()

        if any(process < o[0] for o in os):
            os.append((process, loc))
        else:
            if loc:
                return answer
            answer += 1

    return answer

# 원래는 따로 location 위치를 파악하는 포인터 변수를 두었음
# now_p = location
# now_p = (now_p - 1) % len(os)
# def highest_priorities(process, max):
#     return True if process >= max else False