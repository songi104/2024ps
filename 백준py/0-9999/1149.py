# 백준 1149번 RGB거리
"""
0.5초기 떄문에 O(N2)에 끊어야할 듯

입력
N <= 1000
1번집 r,g,b 비용
2번집 r,g,b 비용
..

출력
모든 집을 칠하는 비용의 최솟값

처음 든 생각은 그리디하게
1번이 제일 작은 비용을 고르고
2번은 그걸 제외하고 제일 작은 비용을 고르고
...
이런 식으로 반복한다.
그때 시간복잡도는 2^N이다.. 너무 많다 너무많다
트리를 그려보니 중복되는 게 보인다. 이걸 이용하자

N부터 1까지 차례대로
n-1에서 d[n-1][0] = min(d[n-1][0] +d[n][1], d[n-1][0]+d[n][2])
# 본인 r 비용과 + n-1 g 비용, 본인 r 비용+n-1 b 비용 중에 작은 거 고른다.

"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
d = {}
for i in range(1, N+1):
    d[i] = list(map(int, input().split()))

print(d)
for i in range(N-1, 0, -1):
    now_r = d[i][0]
    now_g = d[i][1]
    now_b = d[i][2]

    prev_r = d[i+1][0]
    prev_g = d[i+1][1]
    prev_b = d[i+1][2]

    new_r = min(now_r + prev_g, now_r+prev_b)
    new_g = min(now_g + prev_r, now_g+prev_b)
    new_b = min(now_b + prev_g, now_b+prev_r)

    d[i][0] = new_r
    d[i][1] = new_g
    d[i][2] = new_b

print(min(d[1]))
