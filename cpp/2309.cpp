#include <iostream>
#include <algorithm>

using namespace std;

int main() {

    int arr[9];
    int sum=0;

    for (int i = 0 ; i < 9; i++) {
        int k;
        cin >> k;
        arr[i] = k;
        sum += k;
    }

    sort(arr, arr+9);

    // 2명의 키가 sum-100인 경우 찾아서 걔네만 빼고 하면 됨
    for (int i=0; i<8; i++) {
        int t = arr[i];
        for (int j =i+1; j<9; j++) {
            if (arr[i] + arr[j] == sum-100) {
                for (int h=0; h<9; h++) {
                    if (h!=i && h!=j) {
                        cout << arr[h] << '\n';
                    }
                }
                return 0;
            }
        }
    }

}