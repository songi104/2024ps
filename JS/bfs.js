const {temp, graph } = require('./graph.js');

function bfs(graph, v) {
    const visited = []
    const result = []
    let queue = []
    queue.push(v)
    
    while (queue.length) {
        let now = queue.shift()
        visited.push(now)
        result.push(now)
        console.log(now)
        for (node of graph[now]) {
            if (visited.includes(node)) continue;
            //console.log('node:', node);
            queue.push(node)
        }
    }

    return result
}

function main() {
    
    const bfs_result = []
    console.log(graph)
    // let lst = [1,2,3]
    // console.log(lst.shift())
    console.log(bfs(graph, 1))
    
}

main()