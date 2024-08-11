# 백준 1744번 수 묶기
"""
1. 문제
두개씩 묶어서 수열의 최대를 만들어라

2. 아이디어
그냥 큰 것끼리 곱하면 되겠는데?
신경써야할 것: 1, -1, 0
입력받을 때 minus, plus로 나눠서 받고
minus.sort(reverse=True)
plus.sort()
해서 pop으로 꺼내자.
0같은 경우에는 minus에 넣어주자
1의 경우에는 곱하면 손해이니까 그냥 바로 더하자
-1은 그냥 minus에 넣자

3. 시간복잡도, 공간복잡도
"""


"""
1. 문제
수열이 있고 2개씩 묶을 수 있다.
묶는다는 건 곱한다는거다..
최대를 만들어야한다

2. 아이디어
plus끼리 곱하고 (sort... pop 제일큰것들 뽑아서 곱하자)
minus 끼리 곱한다 (sort 제일 작은것들을 뽑아서 곱하자)
신경써야될것: -1, 0, 1
-1 => 그냥 minus
0 => minus
1 => 그냥 바로더해주자


"""


import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
plus = []
minus = []
result = 0
for _ in range(N):
    a = int(input())
    if a > 1:
        plus.append(a)
    elif a <= 0:
        minus.append(a)
    elif a == 1:
        result += 1

plus.sort()
minus.sort(reverse=True)

while len(plus) > 1:
    result += plus.pop() * plus.pop()
while len(minus) > 1:
    result += minus.pop() * minus.pop()
while plus:
    result += plus.pop()
while minus:
    result += minus.pop()

print(result)
