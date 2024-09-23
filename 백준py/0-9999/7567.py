""" 백준 7567번 그릇
queue에서 popleft로 하나씩 꺼낸다.
꺼내면서 now = ( or )
같으면 +5, 다르면 +10
"""

import sys

data = sys.stdin.readline()
print(data)

data = (sys.stdin.readline().rstrip())
print(data)

data = list(sys.stdin.readline().rstrip().split())
print(data)

result = 0
now = ''
for s in data:
    if s == now:
        result += 5
    else:
        now = s
        result += 10

print(result)