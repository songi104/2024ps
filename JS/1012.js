// 백준 1012번 유기농 배추
// ./JS/input.txt -> /dev/stdin

const fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n')
//            .map(line => line.replace('\r', ''))
let input = fs.readFileSync('./JS/input.txt').toString()
        .trim().split('\n');

console.log(input)

// 입력 처리
var T = Number(input[0]);
let line = 1
const result_list = []

for (let t =0; t<T; t++) { // test case 처리
    var [M,N,K] = (input[line].split(' ').map(a => Number(a)));

    //ground 만들기
    var ground = Array(M).fill().map(e => Array(N).fill(0))
    line ++;
    for (let k=0; k<K; k++) {
        let [i, j] = input[line].split(' ').map(a => Number(a))
        ground[i][j] = 1
        line++
    }

    const visited = Array(M).fill().map(e => Array(N).fill(false))
    let result = 0
    // map 돌기
    for (let i=0; i<M; i++) {
        for (let j=0; j<N; j++) {
            //console.log(i,j, visited[i][j])
            if (visited[i][j]) {continue}
            else if ( !visited[i][j] && ground[i][j] === 0 ) {visited[i][j] = true}
            else if ( !visited[i][j] && ground[i][j] === 1) {
                bfs(ground, [i,j], visited)
                result ++
            }
        }
    }

    result_list.push(result)
}

console.log(result_list.join('\n'))

function bfs(ground, v, visited) {
    let [i,j] = v
    let queue = []
    queue.push([i,j])
    
    const dfs = [[1,0], [-1,0], [0,1], [0,-1]]
    while (queue.length) {
        [[i, j], ...queue] = queue;
        //console.log(`bfs`, i, j)
        visited[i][j] = true
        for (let df of dfs) {
            const [dy, dx] = df
            const ny = i+dy 
            const nx = j+dx

            // 범위처리
            if (ny >= M || ny < 0 || nx >= N || nx < 0) {continue;}

            // queue에 넣기
            if (ground[ny][nx] === 0) {visited[ny][nx] = true}
            else if (ground[ny][nx] && visited[ny][nx] ===false) {
                queue.push([ny, nx])
                //console.log(queue)
            }
            //console.log(df)
        }
    }
}
