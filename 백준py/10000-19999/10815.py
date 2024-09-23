# 10815번 숫자카드
"""
숫자카드 N개가 있다. (50만)
정수 M개에 대해 상근이가 가지고있는지 안 가지고 있는지 (50만)

입력
N
N개 숫자카드
M
M개 숫자카드

출력 (가지고있으면 1 없으면 0)
1 0 0 1 1 0 0 1

1. 입력 받기
2. 그냥 각각에 대해서 찾아보기
처음에 이렇게 생각할 수 있을 것이다.
하지만 시간복잡도를 생각해보자. M번 find(O(N)) => MN => N^2이다..
그렇다면? 2500만으로 2초를 넘어간다.
따라서 하나만 줄여보자. NlogN으로 만들자.
이진탐색을 사용하자!

1. 입력 받기
2. 정렬하기
3. 이진탐색으로 찾기 
-> 일단 뭐 한 번 돌리면서 계속 찾는 방법도 있지만
제일 단순한 방법인 각각 원소에 대해서 이진탐색을 사용해보자
"""


import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

# 정렬 -> 시간복잡도는?
numbers.sort()


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return '1'
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return '0'


# 이진탐색
lst = [0]*M
for i in range(M):
    target = targets[i]
    lst[i] = binary_search(numbers, target, 0, N-1)

print(' '.join(lst))
