#include <iostream>

using namespace std;


int main() {
    int arr[21];
    for (int i = 0; i < 21; i++) {
        arr[i] = i;
    }

    //cout << arr;

    for (int i = 0; i < 10; i++) {
        int a, b;
        cin >> a>> b;
        
        // swap part
        while (a < b) {
            swap(arr[a++], arr[b--]);
            }

        // we can use reverse
        // reverse(arr+a, arr+b+1);
    }

    for (int i = 1; i<21; i++) {
        cout << arr[i] << ' ';
    }

    return 0;
}