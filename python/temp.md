올림, 내림, 반올림

### 올림
올림의 경우 math 모듈의 ceil을 사용한다.
```python
math.ceil(3.14) # 결과 4
```


### 내림
내림의 경우 2가지 방법이 있다.
1. 무조건 왼쪽으로 내리는 경우
   이 경우는 수평좌표에서 무조건 작아지는 쪽으로 내린다고 생각하면 된다.
   이 예시에는 math.floor()이 있다.
   ```python
   import math
   math.floor(3.14) # 결과는 3
   ```

2. 0에 가까워지도록 내리는 경우
    math.trunc(), int()가 여기에 해당한다.
    0에 가까워지도록 내리는 것이고 정수부분만 떼어내야할 때 유용하다.
    *사실 이건 음수의 경우 올림이라고도 볼 수 있지만, 어쨌든 내림파트에 집어넣었다.*
    ```python
    import math
    math.trunc(3.14) # 결과는 3
    math.trunc(-3.14) # 결과는 -3
    int(-3.14) # 결과는 -3
    ```


### 반올림
반올림의 경우 내장함수인 round()를 이용하면 된다.
```python
round(3.14) # 결과는 3
```

단, round에서는 알아둬야할 것이 있는데 우리가 아는 반올림 방법이랑 좀 다르다는 것이다.
반올림할 자리 숫자가 5일 때, 앞자리가 짝수면 내림하고 홀수면 올림한다.
이 이유는 대부분의 십진소수가 float으로 정확히 표현될 수 없다는 사실로부터 오는 결과이다.

[출처 파이썬 Docs Round()](https://docs.python.org/ko/3/library/functions.html#round)

[참고자료 (부동소수점산술:문제점 및 한계)](https://docs.python.org/ko/3/tutorial/floatingpoint.html#tut-fp-issues)

아무튼, 쉽게 생각하면 짝수로 맞춰주는 성질이 있다고 생각하면 된다.

```python
round(3.5) # 반올림할 자리 수가 5이고 짝수로 맞춰줘야하므로 결과는 4
round(4.5) # 반올림할 자리 수가 5이고 짝수로 맞춰줘야하므로 결과는 4

round(-3.5) # 앞을 짝수로 맞춰준다고 생각하자! 결과는 -4
round(-4.5) # 앞을 짝수로 맞춰준다고 생각하자! 결과는 -4
```

round는 원래 두 개의 인자를 받는다.
이 때 두번째 인자를 n이라고 하면 round는 소수점 n번째 자리"까지" 반올림해준다.

```python
round(12.3456, 1) # 결과는 12.3
round(12.3456, -1) # 결과는 10.0

round(12.3456) # 결과는 12, int
round(12.3456, 0) # 결과는 12.0, float
```