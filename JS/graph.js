const graph = {
    1: [2,3,4,11],
    2: [1,5,6,7],
    3: [1,9],
    4: [1],
    5: [2,8],
    6: [2],
    7: [2],
    8: [5],
    9: [3,10],
    10: [9],
    11: [1,12],
    12: [11]
}

const temp = {
        1: [2,3],
        2: [1,4],
        3: [1],
        4: [2]
    }

module.exports = {temp, graph}