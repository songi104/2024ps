#include <iostream>

using namespace std;


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string s, t;
    getline(cin, s);
    getline(cin, t);

    int p = t.size();
    int res=0;
    int idx = s.find(t); // 시작위치 반환

    while (idx != string::npos) {
        //cout << "idx: " << idx <<'\n';
        res ++;
        idx = s.find(t, idx+p);
        //cout << "idx: " << idx << '\n';
    }
    cout << res;

    return 0;
}