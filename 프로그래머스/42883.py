def solution2(number, k):
    number = list(map(int, list(number)))
    
    cnt = 0
    i = 0
    while cnt < k:
        #print(i)

        if number[i] < number[i+1]:
            number.pop(i)
            cnt += 1
            i = 0
            #print(number, cnt)
        else: i += 1
        
        if cnt == k: 
            #print('동일!')
            break

        if (i == len(number)): i=0

    result = [str(n) for n in number]
    return "".join(result)

def solution(number, k):
    number_list = list(map(int, list(number)))
    cnt = 0
    max_index = len(number) -1
    for _ in range(2):
        max_num = max(number_list[:max_index])
        max_index = number[:max_index].find(str(max_num))
        print(max_num, max_index)
        





print(solution("4177252841", 4))