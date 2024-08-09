class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_finish(k):
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / k)
            return hours <= h
        
        lo = math.ceil(max(piles) / h)
        hi = max(piles)
        
        while lo <= hi:
            mid = (lo + hi) // 2 # for a language with overflow # mid = lo + (hi - lo) // 2 
            
            if can_finish(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
    
# n = length of piles array
# m = value of the max pile

# Time: O(N log(M))
# Space: O(1)