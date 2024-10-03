# 백준 2143번 두 배열의 합
"""
A의 부배열의 합을 저장하고
B의 부배열의 합을 저장해서
A의 원소 x에 대해
B에서 T-x를 이진탐색을 통해 찾는다.
"""

# 입력 처리
T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# A의 부배열의 합 생성
A_sub_sums = []
for i in range(N):
    current_sum = 0
    for j in range(i, N):
        current_sum += A[j]
        A_sub_sums.append(current_sum)

# B의 부배열의 합 생성
B_sub_sums = []
for i in range(M):
    current_sum = 0
    for j in range(i, M):
        current_sum += B[j]
        B_sub_sums.append(current_sum)

# 두 리스트를 정렬
A_sub_sums.sort()
B_sub_sums.sort()

result = 0


def bs(target):
    pass


for a_sum in A_sub_sums:
    target = T - a_sum
