class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        pos = 0
        neg = 1
        looking_for_positive = True
        for i in range(len(nums)):
            if nums[i] > 0:
                answer[pos] = nums[i]
                pos += 2
            else:
                answer[neg] = nums[i]
                neg += 2
                
        return answer
        