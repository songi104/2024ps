# 큰 수의 법칙

import sys

"""
5 8 3
2 4 5 4 6
"""

N, M, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
print(N, M, K)
lst.sort(reverse=True)

result = 0
biggest_0 = lst[0]
biggest_1 = lst[1]

result += (M//(K+1))*(biggest_0*K + biggest_1)
result += (M % (K+1))*biggest_0

print(result)
