# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
      #  1,2,3,4,5,6,7,8,9,10
      #      G B   
      #          
      #       L H
        
        # 1 2
        # L
        #   H
        # M
        lo = 1
        hi = n
        
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(lo,hi,mid)
            if lo == hi:
                return mid
            elif isBadVersion(mid) :
                hi = mid
            elif lo == mid:
                return hi
            elif hi == mid:
                return lo
            else:
                lo = mid
                
        