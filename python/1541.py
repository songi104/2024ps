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
A, B = map(int, input().split())
M = (B-A)/400
print(1/(1+10**M))