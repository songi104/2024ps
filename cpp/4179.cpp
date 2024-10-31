#include <iostream>
#include <queue>

using namespace std;

int n, m;
string graph[1002];
int fire[1002][1002];
int human[1002][1002];
int dy[4] ={1,0,-1,0};
int dx[4] ={0,1,0,-1};

void fire_bfs(queue<pair<int, int>> Q) {
    while (!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        for (int i=0; i<4; i++) {
            int ny = cur.first + dy[i];
            int nx = cur.second + dx[i];

            // 범위체크
            if (ny <0 || ny >= n || nx <0|| nx >=m) continue;
            if (graph[ny][nx] == '#') continue;
            if (fire[ny][nx] == -1 || fire[ny][nx] > fire[cur.first][cur.second]+1) {
                fire[ny][nx] = fire[cur.first][cur.second] + 1;
                Q.push({ny, nx});
            }
        }
    }
}

int human_bfs(queue<pair<int, int>> Q)
{
    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        int cy = cur.first;
        int cx = cur.second;

        if (cy == 0 || cy==n-1||cx==0||cx==m-1) {
            return human[cy][cx] + 1;
        }

        for (int i = 0; i < 4; i++)
        {
            int ny = cur.first + dy[i];
            int nx = cur.second + dx[i];

            // 범위체크
            if (ny < 0 || ny >= n || nx < 0 || nx >= m || graph[ny][nx] != '.')
                continue;
            if (human[ny][nx] == -1 && (fire[ny][nx] == -1 || fire[ny][nx] > human[cy][cx]+1))
            {
                human[ny][nx] = human[cur.first][cur.second] + 1;
                Q.push({ny, nx});
                }
            }
        }
    return -1;
    }


int main() {

    // 입력받기
    cin >> n>> m;
    for (int i=0; i < n; i++) {
        cin >> graph[i];
        fill(fire[i], fire[i]+m, -1);
        fill(human[i], human[i] + m, -1);
    }


    // 1. Fire bfs-불은 여러개일 수도
    queue<pair<int, int>> Qf;
    queue<pair<int, int>> Qj;
    for (int i = 0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (graph[i][j] == 'F') {
                Qf.push({i,j});
                fire[i][j] = 0;

            }
            else if (graph[i][j] == 'J') {
                Qj.push({i,j});
                human[i][j] = 0;
            }
        }
    }

    // fire bfs
    fire_bfs(Qf);
    int res = human_bfs(Qj);



    if (res == -1) {
        cout << "IMPOSSIBLE";
    } else {
        cout << res;
    }

    return 0;
}