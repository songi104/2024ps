# 백준 열개씩 끊어 출력하기
# 문자열은 범위 초과해도 오류 x
string = input()
i = 0
while i < len(string):
    print(string[i:i+10])
    i+=10
