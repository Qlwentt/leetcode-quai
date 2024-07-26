/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = (nums) => {
  let left = 0

  for (let right = 1; right < nums.length; right++) {
    if (nums[right] !== nums[left]) {
      left++
      nums[left] = nums[right]
    }
  }
  return left + 1
}