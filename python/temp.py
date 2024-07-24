import sys

input = sys.stdin.readline
number = input().rstrip()

def solution(number):
    cute = True

    if len(number) == 1:
        return "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!"

    step = int(number[1]) - int(number[0])
    for i in range(1, len(number)):
        new_step = int(number[i]) - int(number[i-1])
        #print(step, new_step)
        if new_step != step:
            cute = False
            break

    if (cute): 
        return "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!"
    else:
        return "흥칫뿡!! <(￣ ﹌ ￣)>"

#print((number))
print(solution(number))