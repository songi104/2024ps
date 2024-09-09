
from string import ascii_lowercase

S = input().rstrip()
abcs = ascii_lowercase
lst = []
for a in abcs:
    print(S.find(a), end=' ')
