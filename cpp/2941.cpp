#include <iostream>

using namespace std;


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string s;
    cin >> s;
    int i = 0;
    int res = 0;
    while (i < s.size()) {
        string s2 = s.substr(i,2);
        if(s2 == "c=" || s2=="c-" || s2=="d-" || s2=="lj" ||
        s2=="nj" || s2=="s=" || s2=="z=") {
            i += 2;
            res++;
        } else if (s.substr(i,3) == "dz=") {
            i += 3;
            res ++;
        } else {
            i ++;
            res ++;
        }
    }

    cout << res;

    return 0;
}