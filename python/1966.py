# 백준 1966번 프린터 큐
"""
입력:
T 테스트케이스
for _ in range(T):
    N(문서의 개수) M(궁금한 문서의 순서 from 0)
    중요도


Queue이기 때문에 deque로 구현한다. append, popleft
문제에 주어진대로 해보자.
매번 확인하는거다.
처음 중요도에 대해서 뒤에 하나라도 더 큰 게 있다면 뒤로 넘겨보자.
그리고 인쇄할때마다 cnt 를 증가시키면 된다.


궁금한 점:
처음 생각난 방법은 동시에 섞어서 index가 몇 번으로 이동했는지 보면 된다. 이렇게 푼 사람이 있을까?
"""

import sys
from collections import deque
T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    value = (list(map(int, sys.stdin.readline().split())))
    
    cnt = 0
    result = 0
    next_value = []
    i = 0
    while True:
        now = value[i]
        if i == M: # 나는 print될가?
            if (now>=max(value[i:])):
                result += 1
                break
            else:
                value.append(now) 
                M = len(value) -1
        else:
            if (now >= max(value[i:])):
                #value.popleft()
                result += 1
            else:
                value.append(now)         
            i += 1
            cnt += 1
    print(result)