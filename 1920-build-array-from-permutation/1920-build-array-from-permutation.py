class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = [-1] * len(nums)
        for i in range(len(nums)):
            answer[i] = nums[nums[i]]
        return answer