# 백준 1316번 그룹단어체커
"""
입력:
N
N개의 줄

출력: 그룹단어 개수

매번 사전을 이용해서 구현할 수 있음.
단어는 알파벳 소문자로만.
before=now and checker 존재 : ㄱㅊ
before!=now and checker 존재 : X
before!= now and not checker : checker 생성
before=now and checker 미존재: 에러

실수
before = now 까먹음
"""

import sys
input = sys.stdin.readline

N = int(input())

result = 0
for _ in range(N):
    word = input().rstrip()
    checker = {}
    before = ''
    flag = True
    for now in word:
        if before!=now and now not in checker.keys() : checker[now] = True
        elif before!=now and now in checker.keys() :
            
            #print(f'word {word} is not group word\nbefore:{before} now:{now}')
            flag = False
            break
        before = now

    if flag: result += 1

print(result)