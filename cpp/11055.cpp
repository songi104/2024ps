#include <iostream>
#include <algorithm>

using namespace std;


int a[1001];
int dp[1001];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    for (int i =1; i<=n; i++) {
        cin >> a[i];
    }

    dp[0] = 0;
    for (int i =1; i<=n; i++) {
        int maxi = 0;
        for (int j=1; j<=i; j++) {
            if (a[i] > a[j] && maxi < dp[j]) {
                maxi = dp[j];
            }
        }
        dp[i] = maxi + a[i];
    }
    cout << *max_element(dp+1, dp+n+1);

    return 0;
}