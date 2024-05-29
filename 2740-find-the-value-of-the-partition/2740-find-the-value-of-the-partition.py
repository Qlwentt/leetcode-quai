class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        
        nums.sort()
        answer = float('inf')
        for i in range(len(nums)-1):
            answer = min(nums[i+1]-nums[i], answer)
            
        return answer