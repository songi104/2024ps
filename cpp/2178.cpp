#include <iostream>
#include <algorithm>

using namespace std;
string graph[102];
int res[102][102];
int n, m;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m;
    for (int i =0 ; i<n; i++) {
        cin >> graph[i];
    }
    for (int i =1; i<n+1; i++) {
        fill(res[i], res[i]+m, -1);
    }

    // bfs 돌리기

    return 0;

}