import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

lst = list(map(int, input().split()))
ascending = sorted(lst)
des = sorted(lst, reverse=True)

if lst == ascending:
    print('ascending')
elif lst == des:
    print('descending')
else:
    print('mixed')
