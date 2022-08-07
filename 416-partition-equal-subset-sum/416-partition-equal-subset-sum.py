class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = total // 2
        
        for i in range(len(nums) -1, -1, -1):
            newDP = dp.copy()
            for t in dp:
                if nums[i] + t == target:
                    return True
                if t == target:
                    return True
                newDP.add(nums[i] + t)
            dp = newDP
        
        return False
        
        