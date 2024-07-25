import sys

lst = [0, 1, 2, 3, 4]
result = []
for i in range(2, len(lst)):
    for j in range(1, i):
        for k in range(j):
            result.append((i, j, k))
print(result, len(result))
