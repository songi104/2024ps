import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
pokemons = ['']*(N+1)
for i in range(N):
    pokemons[i+1] = input().strip()
# print(pokemons)

for _ in range(M):
    q = input().strip()
    try:
        q = int(q)
        print(pokemons[q])
    except:
        print(pokemons.index(q))
