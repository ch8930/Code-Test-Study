def solution(s):

    check = []
    check.append(s[0])

    for i in s[1:]:
        if i == '(':
            check.append(i)
        else:
            # if not check:
            #     return False
            # check.pop()
            try:
                check.pop()
            except IndexError:
                return False

    return len(check) == 0