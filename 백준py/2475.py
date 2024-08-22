import sys

readline = sys.stdin.readline()

# 1
result = sum(int(i)**2 for i in readline.split())%10
print(result)

# 2
lst = map(int, readline.split())
sqrt_lst = [i**2 for i in lst]
print(sum(sqrt_lst)%10)

# 3
lst = map(int, readline.split())
result = 0
for a in lst:
    result += a**2
print(result%10)