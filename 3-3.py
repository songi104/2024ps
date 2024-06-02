import sys

N, M = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# print(matrix)
result = 0

for i in range(N):
    lst = matrix[i]
    new = min(matrix[i])
    # print(new)
    if new >= result:
        result = new

print(result)
