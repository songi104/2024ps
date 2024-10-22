# 백준 1515번 수 이어쓰기
"""
n을 계속 늘려가면서
line에 겹치는 부분이 있으면 지워준다..

2340라면
n이 2가 됐을 때 2를 지울수있다
그러다가 n이 10이 되면 또 지울 수 있다

근데 23410이면
n이 10이 됐을 때 1 in 10이니까 가능하다
근데 그러면 그 다음 숫자인 0도 지울 수 있는지 그걸 봐야할 듯
차라리 1 == 10인지 보는 게 나을 듯
"""

line = input()
n = 0
while line:
    n += 1
    ss = str(n)
    for s in ss:
        if s == line[0]:
            if len(line) == 1:
                print(n)
                exit(0)
            line = line[1:]
print(n)

# 더 짧은 풀이
# line을 매번 update하지 말고 idx를 도입한다.
line = input()
n = 0
idx = 0
l = len(line)
while True:
    n += 1
    for s in str(n):
        if s == line[idx]:
            idx += 1
            if idx >= l:
                print(n)
                exit()
