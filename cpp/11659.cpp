// 백준 11659번 구간합 구하기 4
#include <iostream>

using namespace std;

int n, m;
int numbers[100001];
int dp[100001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> m;
    for (int i=1; i<n+1; i++) {
        cin >> numbers[i];
    }

    dp[0] = 0;
    for (int i=1; i<=n; i++) {
        dp[i] = dp[i-1] + numbers[i];
    }

    int i, j;
    while (m--) {
        cin >> i >> j;
        cout << dp[j] - dp[i-1] << '\n';
    }


    return 0;
}