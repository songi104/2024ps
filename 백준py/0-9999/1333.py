import sys



# input = sys.stdin.readline
# N, L, D = map(int, input().split())

# last = 0
# result = 0

# for _ in range(N-1):
#     start = last + L
#     last = start + 5
#     k = 1
#     ring = 0
#     while ring < last:
#         ring = k*D + k - 1
#         #print(k, ring, last)
#         if (start <= ring < last):
#             result = ring
#             break
#         k += 1

#     if result != 0 : 
#         break

# if result != 0 :
#     print(result)
# else:
#     time = L*N + 5*(N-1) # 끝나는 시간
#     k = 1
#     while ring < time:
#         ring = k*D + k - 1
#         k += 1
#         if ring >= time:
#             break
#     print(ring)


# 2번째 풀이

input = sys.stdin.readline
N, L, D = map(int, input().split())
lst = [1]*(L*N + 5*(N-1))

# list 만들기
last = 0
for _ in range(N-1):
    start = last + L
    last = start + 5
    lst[start:last] = [0]*5

step = D
time = 0
while True:
    time += step
    if time >= len(lst):
        print(time)
        break
    elif lst[time] == 0:
        print(time)
        break



#print(lst)

