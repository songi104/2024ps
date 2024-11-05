# 백준 1157번
line = input().upper()
d = {}

for s in line:
    if s in d:
        d[s] += 1
    else :
        d[s] = 1

items = list(d.items())
items.sort(key=lambda x:-x[1])
if len(items) == 1:
    print(items[0][0])
elif items[0][1] == items[1][1]:
    print("?")
else:
    print(items[0][0])