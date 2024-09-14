# 백준 14888번 연산자 끼워넣기
"""
N개의 수가 주어진다.
수와 수 사이에 연산자를 하나씩 넣어서 수식을 만든다.
연산자 끼워서 최대, 최소를 정한다.
그냥 앞에서부터 진행하고
나눗셈은 정수 나눗셈으로 몫만 취한다.


0. 입출력
N
N개의 수
+ - x % 의 수

1. 아이디어
트리를 그려서 풀 수 있겠다.
-> 수식을 바로 계산할 수 없는데..
그냥 결과 다 저장하고
최대 최소 빼는 수밖에..

2. 시간복잡도
4+...+4^N
근데 N이 11 이하다.... ㄱㄴ할듯? 다시 찾아보자
11*4^11 이면 4400만이라서 2초안에 가능할듯

3. 자료구조
lst: int[] N개의 숫자 들어있음
results: int[] 연산결과 들어있음 maybe 4^N

"""
import sys


def dfs(n, tres, tsigns):
    global results, lst, N

    if n == N-1:
        results.append(tres)
        return

    # print(f'{n+1}번째 {lst[n+1]}')
    next = lst[n+1]
    # dfs 호출 후에 원래대로 되돌려놔
    if tsigns[0] > 0:
        tsigns[0] -= 1
        dfs(n+1, tres+next, tsigns)
        tsigns[0] += 1

    if tsigns[1] > 0:
        tsigns[1] -= 1
        dfs(n+1, tres-next, tsigns)
        tsigns[1] += 1

    if tsigns[2] > 0:
        tsigns[2] -= 1
        dfs(n+1, tres*next, tsigns)
        tsigns[2] += 1

    if tsigns[3] > 0:
        tsigns[3] -= 1
        # # 나눗셈 처리 (음수인 경우 따로 처리)
        if tres < 0:
            dfs(n+1, -(-tres // next), tsigns)  # 음수 나눗셈 처리
        else:
            dfs(n+1, tres // next, tsigns)      # 양수는 그냥 나눗셈
        tsigns[3] += 1


sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
temp = list(map(int, input().split()))
signs = {}
for i in range(4):
    signs[i] = temp[i]
# print(signs)
results = []


dfs(0, lst[0], signs)  # 0, 연산결과, 남은 부호

# 결과 출력
print(max(results))
print(min(results))
