import sys
input = sys.stdin.readline

lst = []
for _ in range(3):
    lst.append(input().rstrip())

for i in range(3):
    line = lst[i]
    if line[0] in '0123456789':  # 숫자
        result = int(line) + (3-i)
        break

if result % 3 == 0 and result % 5 == 0:
    print('FizzBuzz')
elif result % 3 == 0:
    print('Fizz')
elif result % 5 == 0:
    print('Buzz')
else:
    print(result)
