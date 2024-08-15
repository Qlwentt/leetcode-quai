class Solution:
    def arrangeCoins(self, n: int) -> int:
        
#         rows = 0 
        
#         while n > 0: # -1
#             n -= (rows + 1)
#             rows += 1
            
#         return rows-1 if n < 0 else rows
        
        def is_filled(row):
            return (row * (row+1)) / 2 <= n

        lo = 1
        hi = n                      
        last_complete = None
        while lo <= hi:
            mid = (lo+hi) //2
            if is_filled(mid):
                lo = mid + 1
                last_complete = mid
            else:
                hi = mid - 1
        return last_complete
        
            