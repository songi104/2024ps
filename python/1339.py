# 백준 1339번 단어 수학
"""
영어단어를 숫자로 바꿔서 식을 최대로 만들어야한다.

1. 아이디어
제일 큰 자리수에 많이 나오는 녀석을 9로 주고
점점 줄여나가면 되겠다...
근데 아예 그냥 10**5 이렇게 생각한다음에 하는 건 어떨까?
자릿수별로 몇 번 나왔는지 세어야할 것 같은데..
사전 안에 사전을 넣을까..

"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
words = []
freq = {}
for _ in range(N):
    word = input().rstrip()
    words.append(word)
    l = len(word)
    for i in range(l):
        seat = l - i
        if seat in freq.keys():
            if word[i] in freq[seat].keys():
                freq[seat][word[i]] += 1
            else:
                freq[seat][word[i]] = 1
        else:
            freq[seat] = {word[i]: 1}
# print(words)
# print(freq)

can = list(freq.keys())
can.sort(reverse=True)
result = {}
now = 9
for k in can:
    items = list(freq[k].items())
    items.sort(key=lambda x: [-x[1], x[0]])
    # print(items)
    for i in range(len(items)):
        alpha = items[i][0]
        # print(alpha)
        if alpha not in list(result.keys()):
            result[alpha] = now
            now -= 1
    # print(result)

cnt = 0
for word in words:
    new = ''
    for s in word:
        new += str(result[s])
    cnt += int(new)
print(cnt)
