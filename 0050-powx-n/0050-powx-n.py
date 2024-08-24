class Solution:
    def myPow(self, x: float, n: int) -> float:
#         # 2^10
#         # 2*2*2*2*2 *2*2*2*2*2
#         # 2^5 * 2^5
#         # 2*2*2*2*2
#         # 2^2 * 2^2 *2
#         # 2^2
#         # 2^1 * 2^1
#         # 2^0 * 2
#         # 2^0 = 1
        
        def power(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            halfPower = power(x, n // 2)
            if n % 2: # odd
                return halfPower * halfPower * x
            else: # even
                return halfPower * halfPower
        
        if n < 0:
            return 1/power(x,-n)
        else:
            return power(x,n)

        
        
# Time: O(log(N)) (because halfing every time)
# Space: O(log(N))
        
        
        
       