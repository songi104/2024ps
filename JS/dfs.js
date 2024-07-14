




const {graph} = require('./graph.js')

// 재귀적 구현
function dfs(graph, v, visited, result) {
    visited.push(v);
    //console.log(result)
    result.push(v);
    
    for (let node of graph[v]) {
        if (visited.includes(node)) continue;
        
        //console.log(node)
        dfs(graph, node, visited, result)
    }
    
    return result;
}

function main() {
    const dfs_visited = []
    const dfs_result = []
    dfs(graph, 1, dfs_visited, dfs_result);
    console.log('dfs_result:', dfs_result);

    
}

main()
