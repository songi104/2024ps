# 백준 숫자 카드 2
"""
기존
1. 입력
2. 정렬
3. binary_search

그런데 몇 개 있는지도 알아야한다..사전에 담고 바로바로 접근하면 어떨까?
딕셔너리는 대부분 O(1)이기 때문에 딕셔너리 좋은 듯!

new!
1. 입력
2. 딕셔너리 만들기
3. 그냥 바로 접근하기

근데 시간 제한 1초임..
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

cnt = {}
for num in numbers:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1

result = [0]*M
for i in range(M):
    target = targets[i]
    if target in cnt:
        result[i] = str(cnt[target])
    else:
        result[i] = '0'
print(' '.join(result))
