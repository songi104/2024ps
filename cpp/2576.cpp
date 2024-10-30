# include <iostream>

using namespace std;

int main() {

    int sum, k;
    int prev = 100;
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
    else {
        cout << -1;
    }
}