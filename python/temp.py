import sys

input = sys.stdin.readline

i = 1
while True:
    line = input().rstrip()
    if line == '0':
        break
    r, w, l = map(int, line.split())
    if (2*r)**2 >= (w**2 + l**2):
        print(f'Pizza {i} fits on the table.')
    else:
        print(f'Pizza {i} does not fit on the table.')
    i += 1
