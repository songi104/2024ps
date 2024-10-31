// 


#include <iostream>
#include <queue>

using namespace std;

int t;
int w,h;
string graph[1002];
int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};
int fire[1002][1002];
int human[1002][1002];

int fire_bfs(queue<pair<int,int>> Q) {
    pair<int, int> cur;
    int ny, nx;

    while (!Q.empty()) {
        cur = Q.front(); Q.pop();

        // 상하좌우
        for (int d=0; d<4; d++) {
            ny = cur.first + dy[d];
            nx = cur.second + dx[d];

            if (0<=ny && ny < h && 0<= nx && nx < w && graph[ny][nx] != '#' && fire[ny][nx] == -1) {
                Q.push({ny, nx});
                fire[ny][nx] = fire[cur.first][cur.second] + 1;
            }
        }
    }

    return 0;
}

int human_bfs(int i, int j)
{
    queue<pair<int, int>> Q;
    Q.push({i, j});
    human[i][j] = 1;

    while (!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        for (int d = 0; d < 4; d++)
        {
            int ny = cur.first + dy[d];
            int nx = cur.second + dx[d];
            // 가장자리 도달 시 탈출 성공
            if (ny < 0 || ny >= h || nx < 0 || nx >= w)
            {
                return human[cur.first][cur.second];
            }

            if (graph[ny][nx] == '.' && human[ny][nx] == -1 && fire[ny][nx] > human[cur.first][cur.second] + 1)
            {
                Q.push({ny, nx});
                human[ny][nx] = human[cur.first][cur.second] + 1;
            }
        }
    }

    return -1; // 탈출 불가능한 경우
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> t;
    
    for (int _ = 0; _ < t; _ ++) {
        cin >> w >> h;

        // 입력받기
        for (int i = 0; i < h; i++){
            cin >> graph[i];
            fill(fire[i], fire[i]+w, -1);
            fill(human[i], human[i]+w, -1);
        }

        // cout << "fire" << "\n";
        // for (int i = 0; i < h; i++)
        // {
        //     for (int j = 0; j < w; j++)
        //     {
        //         cout << fire[i][j];
        //     }
        //     cout << endl;
        // }

        // cout << "human" << "\n";
        // for (int i = 0; i < h; i++)
        // {
        //     for (int j = 0; j < w; j++)
        //     {
        //         cout << human[i][j];
        //     }
        //     cout << endl;
        // }

        // 1. 불로 bfs 돌리기 (불은 여러개일 수 있으므로 min으로 fire update)
        queue<pair<int, int>> Q;
        for (int i =0; i<h; i++) {
            for (int j=0; j<w; j++) {
                if (graph[i][j] == '*') {
                    //cout << "meet the fire\n";
                    Q.push({i, j});
                    fire[i][j] = 1;
                }
            }
        }
        fire_bfs(Q);

        // 2. human bfs 돌리기
        bool flag =false;
        for (int i =0; i<h; i++) {
            for (int j=0; j<w; j++) {
                if (graph[i][j] == '@') {
                    int res = human_bfs(i, j);

                    // 3. human에서 가장자리 훑고 0이 아닌 것 중에 min값 + 1
                    // for (int j =0; j < w; j++) {
                    //     res = min(res, (int)human[0][j]);
                    //     res = min(res, (int)human[h-1][j]);
                    // }
                    // for (int i =0; i<h; i++) {
                    //     res = min(res, (int)human[i][0]);
                    //     res = min(res, (int)human[i][w-1]);
                    // }

                    if (res == -1) {
                        cout <<"IMPOSSIBLE\n";
                    } else {
                        cout << res << '\n';
                    }
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }

        

        cout << "fire" << "\n";
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                cout << fire[i][j];
            }
            cout << endl;
        }

        cout << "human" << "\n";
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                cout << human[i][j];
            }
            cout << endl;
    }
}}