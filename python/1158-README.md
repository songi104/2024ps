# 문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

## 입력
N K

## 출력
<3, 6, 2, 7, 5, 1, 4>
요세푸스 순열

# 방법 1
## 구현
numbers = [n for n in range(N+1)]
while True: # len=1이면 그만.
    now 를 정하고 K를 더해서 돌면서 찾기..
    근데 now가 len보다 커지면 len만큼 빼기

이번 사람이 target이라면 지운다.
그리고 target += K 를 하고 target이 len을 넘길 경우를 생각해야한다.
target이 len을 넘긴 순간, 이제 다음 루프로 넘어가는거니까 len(new_numbers)도 넘으면 안 된다.

1. 1부터 N까지 list 0부터 N-1에 넣는다.
2. 완전 처음에만 str(K-1)을 result에 집어넣고 pop한다.
3. 그 후에는 +K를 해준다.
   1. 이 때 target_indx >= len(now) 라면 len(now) 를 빼준다.
   2. 그 후에는 target_index >= len(next) 라면 len(next)를 빼준다.
4. 그렇게 list가 존재할 때까지... 


    
## 실수:
if target > len(numbers) : target - len(numbers)
라고 했는데 여기에는 두가지 문제가 있다.
1. target에 할당해주지 않는다. target -= len(numbers) 라고 해야한다.
2. target에 len-1을 빼야한다. 현재 0이 들어가있어서 len보다 1 크기때문이다.
3. target에 한번만 빼면 나중에 len이 작아지면 target이 생각보다 안 작아지는 문제가 생긴다.
예를 들어 len < K가 되면 K를 더하고 len을 빼면 우리가 원하는 만큼 작아지지않는 것이다.

끝나고 
numbers = new_numbers
new_numbers = []
를 해야하는데 new_numbers를 비워주지않아서 numbers가 계속 늘어났다


## 공부할 것
연결리스트로 구현해야하는가?

deque에서도 pop이 되는가? 시간복잡도는?
deque와 list를 비교하면 좋을 것 같다.

## 알게된 것
result <>로 표현해야할 때 나는 저장을 str 바꿔서했는데 그러지말고.. 다른 것만 replace하자
```
result = str(result).replace('[', '<').replace(']', '>')
```

> 나는 target이 len보다 클 때 로직이 너무 복잡한데 그러지말고 그냥 %를 이용해보자. => 하지만 나의 코드에서는 그런 로직을 이용할 수가 없다. 왜냐하면 나는 다 돌면서 아닌 것을 new_numbers에 추가해주고있기 때문이다. %를 이용하려면 target만 result에 담고 pop을 이용하고, 새로운 리스트에 대해서 %를 하는 게 필요할 듯 싶다.

# 방법 2
1. 1에서 N까지 리스트에 넣는다. index는 0에서 N-1이다.
2. target = K-1이라고 하고 해당하면 result에 넣는다
3. target += K-1에 대해서 result에 넣는다.
4. target >= len(numbers) 라면 % 해줘서 새로운 target을 찾는다.