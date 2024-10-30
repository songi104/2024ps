#include <iostream>

using namespace std;


// 100,000 -> 
// int 는 4B = 32bit = 2**32-1 = 1,000,000,000 ㄱㄴ인데 왜?
// 근데 우리는 10**15까지 해야함. 이것은 10**3**5이니까 2**10**5로 50bit정도가 필요함


int main() {

    long a, b;
    cin >> a >> b;

    long m = min(a, b);
    long M = max(a,b);
    
    if (M-m <= 1) cout << 0;
    else {
        cout << M-m-1 << endl;
        for (long i=m+1; i < M; i++) cout << i << " ";
    }
    return 0;
}