# 백준 2798번 블랙잭

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

result = 0
what = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = numbers[i] + numbers[j] + numbers[k]

            if temp <= M:
                result = max(result, temp)
                what = [numbers[i], numbers[j], numbers[k]]
                why = [i, j, k]
print(result, what, why)
