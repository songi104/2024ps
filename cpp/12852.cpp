// 백준 1로 만들기 2
// 최소 방법과 -> bfs는 어떨가?
// 그 방법을 출력한다

// 일단 지금 생각나는 건 bfs, 백트래킹임..
// dp는 생각나지 않는다.
// 일부러라도 dp는 어떨까? 하고 생각해봐야겠다



#include <iostream>

using namespace std;

int dp[1000001];
int prev_n[1000001];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    dp[0] = 0;
    dp[1] = 0;

    prev_n[0] = 0;
    prev_n[1] = 0;

    for (int i = 2; i <=n; i++) {
        //cout << i<< " calculate \n";
        dp[i] = dp[i-1] + 1;
        prev_n[i] = i-1;

        if (i%2 == 0 && dp[i] > dp[i/2] + 1) {
            dp[i] = dp[i/2] + 1;
            prev_n[i] = i/2;
        }
        
        if (i%3 == 0 && dp[i] > dp[i/3] + 1) {
            dp[i] = dp[i/3] + 1;
            prev_n[i] = i/3; }

    }

    cout << dp[n] <<'\n';
    int cur = n;
    while (true)
    {
        cout << cur << ' ';
        if (cur == 1)
            break;
        cur = prev_n[cur];
    }
        return 0;
    }
