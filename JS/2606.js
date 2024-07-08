//input -> /dev/stdin

const fs = require('fs');
let input = fs.readFileSync('./JS/input.txt').toString().trim().split('\n')
              .map(line => line.replace('\r', ''));
console.log(input);