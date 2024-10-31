#include <iostream>
#include <queue>

using namespace std;

int n, k;
int graph[100001];

int main() {
    
    cin >> n >> k;

    // n이 k가 되는 가장 빠른..
    // 2 곱하거나 +1할 수 있어요
    // bfs 돌리기

    graph[n] = 1;
    queue<int> Q;
    Q.push(n);



    while (!Q.empty()) {
        int cur = Q.front(); Q.pop();
        if (cur == k) {
            cout << graph[k]-1;
            return 0;
        }

        if (2*cur < 100001 && graph[2*cur] == 0) {
            graph[2*cur] = graph[cur] + 1;
            Q.push(2*cur);
        }
        if (cur + 1 < 100001 && graph[cur+1] == 0) {
            graph[cur+1] = graph[cur] + 1;
            Q.push(cur+1);
        }
        if (cur - 1 >= 0 && graph[cur-1] == 0) {
            graph[cur-1] = graph[cur]+1;
            Q.push(cur-1);
        }
    }


    return 0;
}