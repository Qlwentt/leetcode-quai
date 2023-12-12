class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend
        b = divisor
        
        def div(dividend, divisor):
            result = 0
            while dividend >= divisor:
                numToSubtract = divisor
                multiplier = 1
                while dividend >= numToSubtract:
                    dividend -= numToSubtract
                    numToSubtract = numToSubtract << 1
                    result += multiplier
                    multiplier = multiplier << 1
            return result
                
        
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