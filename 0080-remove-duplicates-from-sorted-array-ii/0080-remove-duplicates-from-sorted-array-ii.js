/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let current = nums[0]; // current number being processed
    let count = 1; // count of current number
    let l = 1;

    // note: current could start at nums[0] and count at 1, and l and r at 1,
    // but this is unnecessary since they will just be updated in the second if statement
    
    for (let r = 1; r < nums.length; r++) {
        // if r is at a new num OR the same num as before but it's count is less than 2
        // then we need to record it
        if (current !== nums[r] || count < 2) {
            // overwrite num at l - the sole purpose of l is to know where to overwrite.
            nums[l] = nums[r];
            // increment l after overwriting
            l += 1;
        }

        // we're still on the same r. update current to the new num if applicable.
        if (current !== nums[r]) {
            current = nums[r];
            // naturally, we have to restart the count. 
            // starting at 1, since we updated the num at l already above.
            count = 1;
        } else {
        // otherwise, we're just increasing the count of the same num
            count += 1;
        }
    }
    
    return l;
};