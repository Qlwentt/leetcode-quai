class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        L = 0
        counts = collections.defaultdict(int)
        good = 0
        pairs = 0
        for R in range(len(nums)):
            counts[nums[R]] += 1
            pairs += (counts[nums[R]] - 1)
            while pairs >= k:
                pairs -= (counts[nums[L]] - 1)
                counts[nums[L]] -= 1
                good += len(nums) - R
                L += 1
            
                
        return good
                
            
       #  1 2 3 4 5
       #  0,1,3 6 10
       # 0 1 2 3 4