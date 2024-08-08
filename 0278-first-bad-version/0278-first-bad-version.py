# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        #lowest_bad_version = None
        while lo <= hi:
            mid = (lo+hi) // 2
            
            if isBadVersion(mid):
                hi = mid - 1
                #lowest_bad_version = mid
            else:
                lo = mid + 1
        return lo
        #return lowest_bad_version
        
# Time: O(log(N))
# Space: O(1)
    
    
        