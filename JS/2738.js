const fs = require('fs');
const input = fs.readFileSync('./JS/input.txt').toString().split('\n');
const [N, M] = input[0].replace('\r', '').split(' ').map(Number);
let data = [];

for (let i =1; i< input.length; i++) {
    data.push(input[i].replaceAll('\r', '').split(' ').map(Number));
}
//console.log(data);


let result = [];

for (let i = 0; i<N; i++) {
    result.push([]);
    for (let j=0; j<M; j++) {
        result[i].push(data[i][j] + data[i+N][j]);
    }
    console.log(result[i].join(' '));
}
