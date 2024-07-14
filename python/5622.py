import sys

line = sys.stdin.readline()
dial = {'ABC':2,
        'DEF':3,
        'GHI':4,
        'JKL':5,
        'MNO':6,
        'PQRS':7,
        'TUV':8,
        'WXYZ':9,
        }

#print(dial.keys())
result = 0
for s in line:
    for abc in dial.keys():
        if s in abc:
            result += (1+dial[abc])
            break

print(result)