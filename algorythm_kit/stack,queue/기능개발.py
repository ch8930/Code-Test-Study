from collections import Counter
from itertools import groupby

def solution(progresses, speeds):
    due_date = []

    for p, s in zip(progresses, speeds):
        now = p
        count = 0
        while now < 100:
            now += s
            count += 1
        due_date.append(count)

    for i in range(1, len(due_date)):
        if due_date[i] < due_date[i - 1]:
            due_date[i] = due_date[i - 1]

    return list(Counter(due_date).values())
    # return [len(list(g)) for _,g in groupby(due_date)]