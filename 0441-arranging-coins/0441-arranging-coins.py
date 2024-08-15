class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        row = 1 
        
        while True:
            n -= row
            if n - row <= 0:
                break
            row += 1
            
            
        return row
        
#         def is_filled(row):
#             return (row * (row+1)) / 2 <= n

#         lo = 1
#         hi = n                      
#         # last_complete = None
#         while lo <= hi:
#             mid = (lo+hi) //2
#             if is_filled(mid):
#                 lo = mid + 1
#                 # last_complete = mid
#             else:
#                 hi = mid - 1
#         # return last_complete
#         return hi
        


        
            