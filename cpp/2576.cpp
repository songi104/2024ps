# include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);


    int sum = 0, k, prev = 100;

    for (int i=0; i<7; i++) {
        cin >> k;
        if ( k % 2 == 1 ) {
            sum += k;
            if (k < prev) prev = k;
        }
    }

    // 출력
    if (sum != 0) {
        cout << sum << '\n' << prev;
    }
    else cout << -1;
}