# 백준 2293번 동전 1
"""
제한 0.5초
n <= 100, k<=10000
n3이면 1,000,000 가능

동전을 적당히 더해서 k를 만들어라!!!
경우의 수 구하기

입력
n k
n개의 줄 동전의 가치

작은거부터 늘려서 큰 걸 만들면 된다
트리를 만들 수 있겠는 걸?
트리구조로 표현할 수 있겠다!!

예시로 들자면 1,2,5에서 시작해서
그럼 처음에는 d[1] = 1, d[2] = 1, d[5] = 1이다.
여기서 시작해서 +1, +2, +5할 때마다
예를들어 k에서 1,2,5 더한다고 치면
d[k+1] += d[k]+1
d[k+2] += d[] ..
d[k+5] += ..
그러다 K(목적지)가 될 떄까지 하는거고
큰 for문으로 1부터 k까지 돌리고
for 문으로 1,2,5 n 에 대해서 돌리고


2번째 풀이
예를 들어 10이잖아
10 = 1+9 = 2+8 = 5+5
그러니까 d[10] = d[9] + d[8] + d[5]
근데 여기서 d[n]이 0이라면 계속 작게만들어주면 된다.
return returnD(n) 이런식?
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


# for i in range(1, K+1):
#     for coin in coins:
#         if i+coin > K:
#             continue
#         if i < coin:
#             continue

#         # 더해주는 부분
#         if i+coin in d.keys():
#             d[i+coin] += d[i]
#         else:
#             d[i+coin] = d[i]
#         print(f'{i} + {coin} = {i+coin} {d}')
# print(d[K])


# 두번째 방법
# def returnD(x):
#     print(f'returnD {x}')
#     if d[x] != 0:
#         return d[x]
#     res = 0
#     for coin in coins:
#         if x - coin <= 0:
#             continue
#         print(x, coin)
#         res += returnD(x-coin)
#     d[x] = res
#     return d[x]


# print(returnD(K))


# 입력 읽기
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# DP 테이블 초기화
d = [0] * (K + 1)
d[0] = 1  # 0을 만드는 방법은 아무것도 사용하지 않는 경우 하나뿐

# 모든 동전에 대해 DP 테이블 업데이트
for coin in coins:
    for i in range(coin, K + 1):
        d[i] += d[i - coin]

# 결과 출력
print(d[K])
