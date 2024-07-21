/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let answer = [];
    nums.sort((a,b)=>a-b)
    for (let i=0; i < nums.length; i++) {
        if (i>0 && nums[i-1] == nums[i]) {
            continue
        }
        let a = nums[i]
        let lo = i + 1
        let hi = nums.length - 1
        while (lo < hi) {
            if (a + nums[lo] + nums[hi] > 0) {
                hi--;
            } else if (a + nums[lo] + nums[hi] < 0) {
                lo++;
            } else {
                answer.push([a, nums[lo], nums[hi]])
                lo++;
                hi--;
                while (lo < hi && nums[lo] == nums[lo-1]) {
                    lo++;
                }
                
            }
            
        }
    }
    return answer
    
};