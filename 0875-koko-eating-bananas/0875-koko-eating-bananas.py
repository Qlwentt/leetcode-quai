class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_finish(k):
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / k)
            return hours <= h
        
        lo = 1
        hi = max(piles)
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if can_finish(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo