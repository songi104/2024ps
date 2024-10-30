#include <iostream>
#include <queue>

using namespace std;


int n, m;
int board[502][502];
bool vis[502][502];
int num, res;
int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

int bfs(int y, int x) {
    // 1. Q에 시작점 넣기
    queue<pair<int, int>> Q;
    Q.push({y, x});
    vis[y][x] = true;
    

    int area = 0;
    // 2. Q에서 하나 꺼냄
    while (!Q.empty()) {
        pair<int, int>  cur = Q.front(); Q.pop();
        area ++;
        // 상하좌우로 이동
        for (int d=0; d<4; d++) {
            int ny = cur.first + dy[d];
            int nx = cur.second + dx[d];

            if (!vis[ny][nx] && board[ny][nx] == 1) {
                Q.push({ny,nx});
                vis[ny][nx]= true;
            }
        }    
    }

    return area;
}


int main() {

    //1. 입력
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> board[i+1][j+1];
        }
    }

    int tarea = 0;
    // 2. bfs 돌리고 area 찾아서 저장
    for (int i=1; i<n+1; i++) {
        for (int j=1; j<m+1; j++) {
            if (board[i][j] == 1 && !vis[i][j]) {
                num ++;
                tarea = bfs(i, j);
                res = max(res, tarea);
            }
        }
    }

    cout << num << '\n' << res;


    // 3. area 중에 최댓값 return
}