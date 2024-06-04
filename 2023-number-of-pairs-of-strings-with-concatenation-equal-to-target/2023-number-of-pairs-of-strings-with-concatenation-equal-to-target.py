class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        target_parts = set()
        
        for i in range(1,len(target)):
            a = target[0:i]
            b = target[i:]
            target_parts.add((a,b))
            
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = nums[i]
                b = nums[j]
                if (a,b) in target_parts:
                    answer += 1
                if (b,a) in target_parts:
                    answer += 1
        
        return answer