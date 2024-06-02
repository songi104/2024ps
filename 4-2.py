import sys

N = int(sys.stdin.readline())


# 1. 머리쓰는 버전

result = 0
for h in range(N+1):
    if h == 3 or h == 13 or h == 23:
        # 3:00:00 - 3:59:59 만큼 더하기
        result += 60*60
    else:
        result += 15*(60+60-15)
print(result)


# 2. 단순 탐색

result = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                result += 1


print(result)
