# 백준 14889 스타트와 링크
"""
두 팀으로 나눈다.
능력치 합을 다 더해서 두 팀의 차이가 최소가 되면 된다.

0. 입출력
입력은 N+1의 리스트로 받아야할 듯

1. 아이디어
치킨 문제처럼 우리 팀 기준 속하느냐 안 속하느냐 백트래킹 dfs
그러면 양측의 점수를 계속 넘겨줘야겠는데?

2. 시간복잡도

3. 자료구조
A: int 팀 A의 점수
B: int 팀 B의 점수
matrix: 점수 쓰인 n+1 줄의 list
results: 종료할 때 차이값이 담기는 list


"""

import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
N = int(input())
matrix = [[0]*(N+1)]
for _ in range(N):
    matrix.append([0]+list(map(int, input().split())))
# print(matrix)


def dfs(n, A, B, lstA, lstB):
    global matrix, results

    if n == N+1:
        if len(lstA) == len(lstB) == N//2:
            results.append(abs(A-B))
        return

    # print(n, lstA, lstB)

    # A팀
    score = 0
    for p in lstA:
        score += matrix[p][n]
        score += matrix[n][p]
        # print(f'{n}과 {p}의 케미스트리를 합해요 그럼 {score}')
    dfs(n+1, A+score, B, lstA+[n], lstB)

    # B팀
    score = 0
    for p in lstB:
        score += matrix[p][n]
        score += matrix[n][p]
    dfs(n+1, A, B+score, lstA, lstB+[n])


results = []

dfs(1, 0, 0, [], [])
print(min(results))
