#include <iostream>

using namespace std;



int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int dp[12];
    //fill(dp, dp+12, 0);
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    for (int i =3; i<12; i++) {
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
    }
    int t;
    cin >> t;
    while(t--)
    {int n;
        cin >> n;
        cout << dp[n] <<'\n';
    }
        return 0;
    }