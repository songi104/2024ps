#include <iostream>
#include <vector>

using namespace std;
vector<string> arr;
vector<string> split(string &s, string &sep)
{
    vector<string> res;
    int pos = 0;

    while (pos < s.size())
    {
        int nxt_pos = s.find(sep, pos);
        if (nxt_pos == -1)
            nxt_pos = s.size();
        res.push_back(s.substr(pos, nxt_pos - pos));
        pos = nxt_pos + sep.size();
    }

    return res;
}

bool solve() {
    string f;
    cin >> f;
    if (f.size() < arr[0].size() + arr[1].size()) return 0;
    if (f.find(arr[0]) != 0) return 0;
    int j = f.size() - arr[1].size();
    for (int i=0; i < arr[1].size(); i++) {
        if (arr[1][i] != f[j++]) return 0;
    }
    return 1;

}



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    string pattern, s;
    string sep = "*";
    cin >> n;
    cin >> pattern;
    arr = split(pattern, sep);

    while (n--) {
        if (solve()) cout << "DA\n";
        else cout << "NE\n";
    }

    return 0;
}