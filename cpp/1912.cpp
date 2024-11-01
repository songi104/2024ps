#include <iostream>
#include <algorithm>

using namespace std;

int a[100001];
int dp[100001];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for(int i=1; i<=n; i++) {
        cin >> a[i];
    }

    // dp
    dp[0] = 0;
    for (int i=1; i<=n; i++) {
        dp[i] = max(0, dp[i-1]) + a[i];
    }

    cout << *max_element(dp+1, dp+n+1);

    return 0;
}