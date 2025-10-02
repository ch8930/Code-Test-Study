from collections import deque

# 큐 자료구조로 변환해서 문제 풀이
def solution(queue1, queue2):
    answer = 0

    total = sum(queue1) + sum(queue2)

    if total % 2 != 0:
        return -1

    q1 = deque(queue1)
    q2 = deque(queue2)

    max_count = 3 * len(q1)
    sum1 = sum(q1)
    sum2 = sum(q2)

    while answer <= max_count and q1 and q2 :

        if sum1 == sum2:
            return answer

        if sum1 > sum2:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x

        else:
            x = q2.popleft()
            q1.append(x)
            sum1 += x
            sum2 -= x

        answer += 1

    return -1

# 인덱스 기반으로 문제 해결방법
def solution2(queue1, queue2):
    answer = 0

    total = sum(queue1) + sum(queue2)

    if total % 2 != 0:
        return -1

    target = int(total/2)
    q = deque(queue1 + queue2)

    s = 0
    e = len(queue1) - 1

    sum_value = sum(queue1)

    while s <= e and e < len(q):

        if sum_value == target:
            return answer

        if sum_value > target:
            sum_value -= q.popleft()
            s += 1
        else :
            e += 1
            sum_value += q[e]

        answer += 1

    return -1