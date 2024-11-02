#include <iostream>
#include <queue>
#define Y first
#define X second

using namespace std;

int dy[8] = {-2, -2, 2, 2, -1, 1, -1, 1};
int dx[8] = {1, -1, 1, -1, 2, 2, -2, -2};
int graph[301][301];
int t, l;

int bfs(int a, int b, int c, int d) {
    // 8가지 방향에 대해서
    // 범위 체크, 방문했는지 체크, 그 후 update
    queue<pair<int, int>> Q;
    Q.push({a,b});
    graph[a][b] = 0;

    while (!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        int cy = cur.Y;
        int cx = cur.X;
        if (cy == c && cx == d)
            return graph[cy][cx];

        for (int i =0; i<8; i++) {
            int ny = cy + dy[i];
            int nx = cx + dx[i];

            if (ny < 0 || ny >= l || nx < 0 || nx >= l) continue;
            if (graph[ny][nx] != -1) continue;
            graph[ny][nx] = graph[cy][cx] + 1;
            Q.push({ny, nx});

            
        }
    }
    return -1;
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int a, b, c, d;
    cin >> t;

    while (t--) {
        cin >> l;
        cin >> a >> b; // 출발지
        cin >> c >> d; // 목적지

        for (int i=0 ; i<=l; i++ ) {
            fill(graph[i], graph[i] +l, -1);
        }

        cout << bfs(a,b,c,d) << '\n';
    }


    return 0;
}