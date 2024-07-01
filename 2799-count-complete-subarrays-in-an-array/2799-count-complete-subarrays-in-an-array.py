class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        answer = 0
        for i in range(len(nums)):
            sub_array = set()
            for j in range(i,len(nums)):
                sub_array.add(nums[j])
                answer += len(sub_array) == target
        return answer
        
         
        