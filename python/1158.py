# 백준 1158번 요세푸스 문제

"""



입력:
N K

출력:
<3, 6, 2, 7, 5, 1, 4>
요세푸스 순열

구현:
numbers = [n for n in range(N+1)]
while True: # len=1이면 그만.
    now 를 정하고 K를 더해서 돌면서 찾기..
    근데 now가 len보다 커지면 len만큼 빼기

이번 사람이 target이라면 지운다.
그리고 target += K 를 하고 target이 len을 넘길 경우를 생각해야한다.
target이 len을 넘긴 순간, 이제 다음 루프로 넘어가는거니까 len(new_numbers)도 넘으면 안 된다.

    
실수:
if target > len(numbers) : target - len(numbers)
라고 했는데 여기에는 두가지 문제가 있다.
1. target에 할당해주지 않는다. target -= len(numbers) 라고 해야한다.
2. target에 len-1을 빼야한다. 현재 0이 들어가있어서 len보다 1 크기때문이다.
3. target에 한번만 빼면 나중에 len이 작아지면 target이 생각보다 안 작아지는 문제가 생긴다.
예를 들어 len < K가 되면 K를 더하고 len을 빼면 우리가 원하는 만큼 작아지지않는 것이다.

끝나고 
numbers = new_numbers
new_numbers = []
를 해야하는데 new_numbers를 비워주지않아서 numbers가 계속 늘어났다
"""

import sys

N, K = map(int, sys.stdin.readline().split())
numbers = [n for n in range(N+1)]
new_numbers = []

target = K
now = 0
result = []

while True:
# for _ in range(4):
    #print(numbers)
    for i in range(len(numbers)):
        if i == target:
            #print(f'target {target}, {numbers}, next_target: {target+K}')
            result.append(str(numbers[i]))
            target += K
            #print(result)
        else: 
            new_numbers.append(numbers[i])
            #print(f'new_number: {new_numbers}')
    
    #print(f'현재 target은 {target}')
    while target >= len(numbers):
        if target <= 0: target+= K
        target = target - (len(numbers)-1)
    #print(f'target을 {target}으로 변경했어요')
    #print(f'------------------한바퀴 끝 result: {result}')
    numbers = new_numbers
    new_numbers = []
    if len(numbers) == 1: break


print("<"+', '.join(result)+">")