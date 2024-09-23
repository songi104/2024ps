# 백준 1158번 요세푸스 문제

import sys

N, K = map(int, sys.stdin.readline().split())
numbers = [n+1 for n in range(N)]
#print(numbers)

target = K-1
result = []
i = 0
new_numbers =[]

while numbers:
    #print(f'target index: {target}')
    if i == target:
        #print(f'{i}=={target}')
        result.append((numbers[target]))
        #print(f'result에 {numbers[target]} 추가')
        target += K
    else:
        new_numbers.append(numbers[i])

    # i 범위 검사
    i += 1

    if i == len(numbers):
        i = 0
        # target 범위 검사
        if target >= len(numbers):
            target -= len(numbers)
            numbers = new_numbers
            new_numbers = []

            while target >= len(numbers) and numbers:
                target -= len(numbers)


#print("<"+', '.join(result)+">")
result = str(result).replace('[', '<').replace(']', '>')
print(result)

