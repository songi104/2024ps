# 백준 1744번 수 묶기
"""
수열을 2개씩 묶을 수 있다. 묶는다는 건 괄호를 쳐서 곱한다는 뜻이다.
-> 큰 순서대로 묶으면 되겠는데?
N (50보다 작은 자연수)
N줄 (-1000<=x<=1000)

2. 아이디어
* 입력처리
- 마이너스는 마이너스대로 냅두고
- 0은 0대로 냅두고 (걍 버려) -> ㄴㄴ 마이너스쪽에 해주면 좋다
- 플러스는 플러스대로 묶는다

* 정렬
플러스는 오름차순 (pop으로 꺼내자)
마이너스는 reverse (pop으로 꺼내자)
해서 처음부터 2개씩 곱하면서 꺼내고 (짝/홀 처리 잘하기)
result에 다 더해주기

* 남은 거 처리
"""

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
minus = []
plus = []
result = 0
for _ in range(N):
    a = int(input())
    if a <= 0:
        minus.append(a)
    elif a == 1:
        result += a
    elif a > 0:
        plus.append(a)


# 정렬
minus.sort(reverse=True)
plus.sort()
# print(plus, minus)


# 꺼내면서 곱한다
while len(plus) >= 2:
    result += plus.pop()*plus.pop()
    # print(result)
while len(minus) >= 2:
    result += minus.pop()*minus.pop()
    # print(result)

while len(plus) > 0:
    result += plus.pop()
while len(minus) > 0:
    result += minus.pop()

print(result)
