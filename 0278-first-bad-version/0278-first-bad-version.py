# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        lowest_bad = None
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if isBadVersion(mid):
                lowest_bad = mid
                hi = mid - 1
            else:
                lo = mid + 1
                
        return lowest_bad
        