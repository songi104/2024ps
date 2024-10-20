T = int(input())
for _ in range(T):
    line = input().rstrip().replace(' ', '')
    cnt = {}

    # count 세기
    for n in line:
        if n in cnt:
            cnt[n] += 1
        else:
            cnt[n] = 1

    # 젤 큰 놈 return
    items = list(cnt.items())
    items.sort(key=lambda x: x[1], reverse=True)

    if len(items) == 1 or items[0][1] != items[1][1]:
        print(items[0][0])
    else:
        print('?')
