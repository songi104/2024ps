#include <iostream>
#include <vector>

using namespace std;

vector<string> split(string& s, string& sep) {
    vector<string> res;
    int pos = 0;

    while(pos < s.size()) {
        int nxt_pos = s.find(sep, pos);
        if (nxt_pos == -1) nxt_pos = s.size();
        res.push_back(s.substr(pos, nxt_pos-pos));
        pos = nxt_pos + sep.size();
    }

    return res;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string s;
    string sep;

    cin >> s;
    cin >> sep;
    vector<string> res = split(s, sep);
    for (auto r: res) {
        cout << r << '\n';
    }


    return 0;
}