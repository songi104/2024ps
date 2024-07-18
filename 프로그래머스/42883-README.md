# 문제
## 문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하자.
ex) 1924에서 수 두개를 제거하면 ... 이 중 가장 큰 숫자는 94이다.

## 입력과 출력
문자열 형식으로 숫자 number와 
제거할 수의 개수 k가 solution의 매개변수로 주어집니다.
가장 큰 숫자를 문자열 형태로 return

# 구현
1. 문자열의 개수를 센다 n
2. n-k로 몇 개의 숫자로 만들어야하는지 구한다
3. 문자열을 리스트에 넣고 정렬한 다음 가장 큰 녀석부터 합쳐서 return
=> 완전 잘못된 풀이!

어떻게 지우는 기준을 마련할 수 있을까?
1. 앞에부터 i로 돌면서
2. i+1 자리가 더 크다면 그녀석을 빼도 된다.
3. k번 빼면 break

cnt = 0
while cnt < k:
    for i in range(len(number)-1):
        if number[i] < number[i+1]:
            delete number[i]
            cnt += 1
            if cnt == k: break
=> 이것도 불가하다! 예를들어 417712 를 생각해보면 41을 다 빼야하는데 1만 빠진다.

max를 이용해보자. max 앞부분의 개수가 k-cnt보다 작으면 다 날려도 된다.

# 더 공부할 것
number = "1924" 일 때 나는 [1,9,2,4]를 원한다면 만드는 방법은?
```python
number = list(map(int, list(number)))
```

list의 pop 시간복잡도는?

find 정리하기


# 실수
number라는 문자열에서 k개의 수를 제거하는 것이다. 그냥 그것을 list로 만들어서 하면 안 된다..

number.pop을 하면 number의 list 개수가 달라져서 곤란하게 된다. 이걸 해결할 방법은 무엇일까?
1. 새로운 리스트를 만든다
2. try-catch 사용한다