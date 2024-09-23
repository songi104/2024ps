# 백준 1546번 평균

"""
1. 입력 처리
    1. 과목개수 N
    1. 현재 성적들 a b c ...
1. max 찾기
1. for문 돌면서 max 기반으로 결정하고 새로운 list에 넣기
1. sum 함수 이용해서 평균 구하기

생각해볼 것
1. list에 한 번에 함수를 적용하는 방법은 없을까?
좀 더 빠르다면 이걸 이용할 수 있을 것 같다
1. max, min <-> math library
"""


import sys
import math

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
max_score = max(scores)
#print(max_score)

new_scores = []
for score in scores:
    new_scores.append(score/max_score*100)
print(sum(new_scores)/N)
