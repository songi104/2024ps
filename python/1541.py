# 백준 1541번 잃어버린 괄호

"""
알고리즘을 생각해보자,,
만일 모두 +라면 상관이 없다.
그러나 -가 있을 때가 핵심인데,
- 뒤의 수를 최대한 크게 만들면 된다...
마지막 - 다음에 괄호를 치자.


"""
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
line = input().rstrip()
N = len(line)
#print(f'origin: {line}')

res = 0
chunk = 0
num = ''
for i in range(N-1, -1, -1):
    s = line[i]
    if s == '+':
        chunk += int(num)
        num = ''
    elif s=='-':
        chunk += int(num)
        res -= chunk
        chunk =0
        num =''
    else:
        num  = s + num
if chunk != 0:
    res += chunk
res += int(num)
print(res)