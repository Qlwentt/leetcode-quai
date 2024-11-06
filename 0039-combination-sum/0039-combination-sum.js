/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const ans = [];
    function backtrack(index, path, curSum) {
        if (curSum === target) {
            ans.push([...path])
            return;
        }

        if (curSum > target) {
            return;
        }

        for (let i = index; i < candidates.length; i++) {
            path.push(candidates[i]);
            backtrack(i, path, curSum + candidates[i]);
            path.pop();
        }
    }

    backtrack(0, [], 0)
    return ans;





};