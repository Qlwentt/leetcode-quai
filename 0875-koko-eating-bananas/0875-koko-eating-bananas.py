class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #   [3,6,7,11]
    # 3// 1 + 6//1 + 7//1 + 11//1
    # 3//min(3,4) + 6 // (4,6) 

        def getHours(k):
            hours = 0            
            for pile in piles:
                hours += (pile // min(k,pile)) + (pile % min(k,pile) != 0)
            return hours
        # 11,10,9,9,8,7,7,6,6,6,6,6,5,5,5,5,5
        #               L       H           H
        
        lo = 1
        hi = max(piles)
        
        while lo < hi:
            mid = (lo + hi) // 2
            hours = getHours(mid)
            if hours > h: # k(mid) is too fast(high)
                lo = mid + 1
            else: # k(mid) is too slow (low)
                hi = mid
        return lo # first instance of hours == h
            
    
        