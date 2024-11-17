# 백준 팰린드롬인지 확인하기

string = input()
left = 0
right = len(string)-1
while left <= right:
    if string[left] == string[right]:
        left += 1
        right -= 1
        continue
    else:
        print(0)
        exit()
print(1)
