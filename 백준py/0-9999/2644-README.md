# 문제
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

## 입력
전체 사람의 수 n
촌수 계산해야하는 두 사람 번호
관계의 개수 m
x(부모) y(자식) m줄

## 출력
촌수 (없다면 -1)

# 구현
## BFS
토마토 문제처럼 cnt를 기록하자. 
result = [0]*(n+1) 해서 a에서 bfs를 돌리고 cnt를 result에 기록한다. 그러다가 b를 만나면 멈춘다. 정답은 result[b]이고 만약 b를 만나지 못했다면 -1 출력한다.

>1. 입력처리 및 세팅 (graph, visited, result) -> 일단 visited 해보고 더 발전시킬 여지는 graph에서 0으로 표현할 수 있는지?
>2. a 에서 bfs 돌리기
>3. result[b] 출력 만약 0이라면 -1 출력

### 질문
result에서 min 처리를 해주어야하는가? 어디선가 더 일찍 도착할수 있는가?... 없다! min 처리를 안 해줘도 될 것 같아 (논리로 확인해보기)

## DFS
