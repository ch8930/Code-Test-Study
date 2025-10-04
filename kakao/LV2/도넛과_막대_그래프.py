from collections import defaultdict
import sys
# 파이썬에서는 재귀 제한이 있어서 재귀리밋을 설정해줘야 함
sys.setrecursionlimit(10 ** 6)


def solution(edges):
    graph_in = defaultdict(int)
    graph_out = defaultdict(list)
    answer = [0] * 4
    visited = set()

    for x, y in edges:
        graph_out[x].append(y)
        graph_in[y] += 1

    # 생성 정점 찾기
    for x in graph_out:
        if len(graph_out[x]) >= 2 and graph_in[x] == 0:
            answer[0] = x
            break

    for g in graph_out[answer[0]]:
        type = check_graph_type(g, visited, graph_out)
        answer[type] += 1

    return answer


def check_graph_type(node, visited, graph_out):
    if node in visited:
        return 1
    visited.add(node)

    if len(graph_out[node]) == 2:
        return 3
    if not graph_out[node]:
        return 2
    return check_graph_type(graph_out[node][0], visited, graph_out)


"""
다른 풀이 방식
"""

def solution2(edges):
    graph = defaultdict(list)
    graph_out = defaultdict(int)
    graph_in = defaultdict(int)
    visited = set()
    answer = [0] * 4
    n = 0

    for x, y in edges:
        n = max(n, max(x, y))
        graph[x].append(y)
        graph_out[x] += 1
        graph_in[y] += 1

    total = 0

    for i in range(1, n + 1):
        if graph_out[i] >= 2 and graph_in[i] == 0:
            answer[0] = i
            total = graph_out[i]

        elif graph_out[i] == 2 and graph_in[i] >= 2:
            answer[3] += 1
        elif graph_out[i] == 0 and graph_in[i] >= 1:
            answer[2] += 1

    answer[1] = total - (answer[2] + answer[3])

    return answer


