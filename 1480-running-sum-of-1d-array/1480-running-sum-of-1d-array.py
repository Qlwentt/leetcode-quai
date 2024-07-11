class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = 0
        answer = []
        
        for num in nums:
            current_sum += num
            answer.append(current_sum)
        
        return answer
        