import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    string = input().rstrip()
    flag = False
    res = 0
    chunk = 0
    for s in string:
        if s == 'O':
            chunk += 1
            res += chunk
            flag = True
        else:  # X일 때
            flag = False
            chunk = 0
    print(res)
