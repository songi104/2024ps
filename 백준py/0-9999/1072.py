# 백준 1072번 게임

"""
입력
X 게임 횟수 10
Y 이긴 게임 8

출력
몇 판 더해야 Z가 변하는가?

1. 현재 승률을 계산한다.
2. 0부터 X 중에 z 가 변하는 최소를 찾는다.
    변하지 않았다면 start를 옮겨주고
    변했다면 end를 옮겨준다

    
edge:
99에서는 변할 수 없다. z >= 99 라면 -1 출력하기
98에서는 어떻니? 가능할 것 같긴한데..
최대 x로 이분탐색 ㄱㄱ
"""


x, y = map(int, (input().split()))
z = int((y*100/x))


def solution():
    if z >= 99:
        return -1

    # 이분탐색
    start = 0
    end = 2000000000
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        new_z = int((y+mid)/(x+mid)*100)
        if new_z > z:
            ans = mid
            end = mid - 1
        elif new_z <= z:
            start = mid + 1
    return ans


print(solution())
