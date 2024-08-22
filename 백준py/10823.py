# 백준 10823번 더하기 2

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readlines

lst = input()
string = ''
for word in lst:
    string += word.rstrip()
lst = list(map(int, string.split(',')))
result = 0
for n in lst:
    result += n
print(result)
