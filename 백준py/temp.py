import sys


lst = set()
for _ in range(10):
    lst.add(int(input()) % 42)
print(len(lst))
