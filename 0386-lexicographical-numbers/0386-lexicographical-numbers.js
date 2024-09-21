/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    array = []
    for (let i = 1; i < n + 1 ; i++) {
        array.push(i)
    }
    return array.sort()
};