class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        L = 0
        window = collections.defaultdict(int)
        answer = 0
        for R in range(len(nums)):
            window[nums[R]] += 1
            while len(window) == target:
                answer += (len(nums) - R)
                window[nums[L]] -= 1
                if window[nums[L]] == 0:
                    del window[nums[L]]
                L += 1
                
            
            
        return answer
                
        
         
        