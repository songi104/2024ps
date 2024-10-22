"""
1. N, M
2. input M 이상이면 pass
3. count 만들기
"""

import sys
input = sys.stdin.readline
words = {}

N, M = map(int, input().split())
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue

    # 단어장 추가
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

items = list(words.items())
items.sort(key=lambda x:(-x[1], -len(x[0]), x[0]))
for a, b in items:
    print(a)