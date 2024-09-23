a, b = map(int, input().split())
min_num = min([a, b])
max_num = a*b

# 최대공약수
candidate = 1
for i in range(1, min_num+1):
    if (a % i == 0 and b % i == 0):
        candidate = i
print(candidate)

# 최소 공배수
candidate = max_num
for i in range(min_num, max_num+1):
    if (i % a == 0 and i % b == 0):
        candidate = i
        break
print(candidate)
