from itertools import combinations, product
from bisect import bisect_left, bisect_right

def solution(dice):
    answer = []
    candidates = list(combinations(dice, int(len(dice) / 2)))

    max_win = 0
    for c in candidates:
        now_dice = []
        b_choice = []
        for i, d in enumerate(dice):
            # A가 선택
            if d in c:
                now_dice.append(i + 1)
            else:
                b_choice.append(d)

        win_count = play_game(c, b_choice)
        if win_count > max_win:
            max_win = win_count
            answer = now_dice

    return answer


def play_game(a_choice, b_choice):
    win = 0
    a_pair = [sum(p) for p in product(*a_choice)]
    b_pair = [sum(p) for p in product(*b_choice)]

    b_pair.sort()

    for i in a_pair:
        # x = bisect_left (b_pair, i)
        x = find_left_index(b_pair, i)
        win += x

    #     a_b_pair = [(x,y) for x in a_pair for y in b_pair]

    #     for x,y in a_b_pair:
    #         if x > y:
    #             win += 1

    return win


def find_left_index(list, v):
    start = 0
    end = len(list)

    while start < end:
        target = (start + end) // 2
        if list[target] < v:
            start = target + 1
        else:
            end = target

    return start


