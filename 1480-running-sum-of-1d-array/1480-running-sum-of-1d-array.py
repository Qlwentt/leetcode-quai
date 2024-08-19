class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum = 0
        answer = []
        for num in nums:
            cur_sum += num
            answer.append(cur_sum)
        return answer
# # Time: O(N)
# Space: O(N) counting the output

# in place
# might not be considered best practice to alter an array while you are iterating through it

        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i] 
            nums[i] = cur_sum
        return nums
# Time: O(N)
# Space: O(1)

