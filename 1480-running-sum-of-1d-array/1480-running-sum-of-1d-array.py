class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum = 0
        answer = []
        for num in nums:
            cur_sum += num
            answer.append(cur_sum)
        return answer
# Time: O(N)
# Space: O(N) counting the output