string = input()
N = len(string)

i = 0
res = ""
while True:
    s = string[i]
    if s == "<":
        j = string.find(">", i)
        res += string[i:j+1]
        i = j
        
    elif s != " ":
        j = min(string.find(" ", i), string.find("<", i))
        word = list(string[i:j+1])
        word.reverse()
        res += ''.join(word)
        i = j
    else:
        print(f"else: {s}")
    print(res)

