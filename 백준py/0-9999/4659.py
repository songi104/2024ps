# 백준 4659번 비밀번호 발음하기
import sys
input = sys.stdin.readline


def check(word):
    # 1. aeiou 중 하나를 반드시 포함
    if 'a' not in word and 'e' not in word and 'i' not in word and 'o' not in word and 'u' not in word:
        return False

    # 2. 모음이 3개 혹은 자음이 3개 연속 오면 안 됨
    # 모음 - 0 자음 1로 표현
    p = -1
    pp = -1
    if len(word) >= 3:
        if word[0] in 'aeiou':
            pp = 0
        else:
            pp = 1

        if word[1] in 'aeiou':
            p = 0
        else:
            p = 1

        i = 2
        while True:
            if len(word) <= i:
                break

            now = 0 if word[i] in 'aeiou' else 1
            # 3개 비교
            if p == pp and p == now:
                return False

            pp = p
            p = now
            i += 1

        # 3. 같은 글자 연속 두번 안 됨 (단, ee, oo 제외)
        if len(word) == 1:
            return True

        p = word[0]
        for n in word:
            if n == p and (n != 'e' and n != 'o'):
                return False
            p = n
        return True


while True:
    word = input().rstrip()
    if word == 'end':
        break

    # check 알고리즘
    flag = check(word)

    # 결과 출력
    if flag:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')
