"""
다섯개의 line.
max 15 즉 range(15)로
lst[0][i]로 돌기
이 때 lst len이 넘으면 pass
"""
import sys
input = sys.stdin.readline
lst = []
lens = []
for _ in range(5):
    word = input().rstrip()
    lst.append(word)
    lens.append(len(word))

# 돌면서 결과
res = ''
for i in range(15):
    for j in range(5):
        if lens[j] <= i:
            continue
        res += lst[j][i]
print(res)
