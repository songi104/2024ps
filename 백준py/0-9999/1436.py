N = int(input())

cnt = 1
num = 666

while True:
    if cnt == N:
        res = num
        break
    num += 1
    if '666' in str(num):
        cnt += 1

print(res)
