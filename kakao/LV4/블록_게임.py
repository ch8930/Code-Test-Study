def solution(board):
    answer = 0
    # 도형 개수 출력
    num = max(max(row) for row in board)

    candidates_pos = []
    candidates_num = []

    # 후보 도형 추출
    for x in range(1, num + 1):
        positions = [(i, j) for i, row in enumerate(board) for j, v in enumerate(row) if v == x]

        # 해당 번호의 도형이 없으면 pass
        if not positions:
            continue

        candidates_pos, candidates_num = check_block_type(positions, x, candidates_pos, candidates_num)

    count = 0
    # 모든 도형을 다 탐색했으면 종료
    while count < len(candidates_pos):
        for p, n in zip(candidates_pos, candidates_num):
            if check_possible(p, board) and check_up(p, board):
                delete_block(board, n)
                candidates_pos.remove(p)
                candidates_num.remove(n)
                answer += 1
                count = 0
                break
            else:
                count += 1

    return answer


def check_block_type(positions, num, candidates_pos, candidates_num):
    # 직사각형이 될 수 있는 후보 블록
    possible_block = [
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 1), (2, 0), (2, 1)],
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 2), (1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 0), (1, 1), (1, 2)],
    ]

    # 후보 블록에 떨어트려야 하는 검은 블록 위치
    check_block = [
        [(0, 1), (0, 2)],
        [(0, 0), (1, 0)],
        [(0, 1), (1, 1)],
        [(0, 0), (0, 1)],
        [(0, 0), (0, 2)]
    ]

    # 정규화 목적
    min_row = min(r for r, c in positions)
    min_col = min(c for r, c in positions)

    nor_positions = normalized_position(positions, min_row, min_col)

    for p, c in zip(possible_block, check_block):
        if nor_positions == p:
            check = []
            for row, col in c:
                check.append((row + min_row, col + min_col))

            candidates_pos.append(check)
            candidates_num.append(num)

    return candidates_pos, candidates_num


def normalized_position(positions, row, col):
    return [(r - row, c - col) for r, c in positions]


# 다른 블록이 없는지 확인
def check_possible(positions, board):
    x1, y1 = positions[0]
    x2, y2 = positions[1]
    return board[x1][y1] == 0 and board[x2][y2] == 0


# 막는 블록이 있는지 확인
def check_up(positions, board):
    for x, y in positions:
        for r in range(x):
            if board[r][y] != 0:
                return False
    return True


# 사각형이 되면 삭제
def delete_block(board, n):
    for i, r in enumerate(board):
        for j, v in enumerate(r):
            if v == n:
                board[i][j] = 0


