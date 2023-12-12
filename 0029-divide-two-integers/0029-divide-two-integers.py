class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # write a function for multiplying recursively using addition
        # get number that you can multiply divisor by to get dividend without going over using binary search
        # handle negatives
        
        
        a = dividend
        b = divisor
        
        def div(dividend, divisor):
            lo = 0
            hi = dividend
            
            while lo <= hi:
                
                mid = (lo + hi) >> 1 # get midpoint without division
                attempt = self.multiply(divisor, mid)
                if attempt < dividend:
                    lo = mid + 1
                elif attempt > dividend:
                    hi = mid - 1
                else:
                    return mid
            
            return hi
        
        if a < 0 and b < 0:
            answer = div(-a,-b)
        elif a < 0 or b < 0:
            
            answer = -div(abs(a),abs(b))
        else:
            answer = div(a,b)
            
        if answer > 2 ** 31 -1:
            return 2 ** 31 -1
        elif answer < -(2 ** 31):
            return -(2 ** 31)
        else:
            return answer
            
        
        
    def multiply(self, a, b):
        def isOdd(n):
            return not ((n >> 1) << 1 == n)
        product = 0
        while b > 0:
            if isOdd(b):
                product += a
            a = a << 1
            b = b >> 1
        return product
        
        
    
    
        
        