#include <iostream>

using namespace std;

int n, m;
int tlst[8];


void dfs(int num, int l) {
    

    if (l == m) {
        for (int i =0; i<m; i++) {
            cout << tlst[i] << " ";
        }
        cout << "\n";
        return;
    }

    if (num == n+1) {
        return;
    }

    
    tlst[l] = num;
    dfs(num+1, l+1);
    
    tlst[l] = 0;
    dfs(num+1, l);

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;
    fill(tlst, tlst+8, 0);
    dfs(1, 0);
    return 0;
}