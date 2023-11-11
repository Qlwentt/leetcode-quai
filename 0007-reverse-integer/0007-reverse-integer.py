class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = (2 ** 31) - 1
        
        def rev(x):
            answer = 0
            while x:
                digit = x % 10
                
                # overflow
                if answer > INT_MAX//10 or answer == INT_MAX//10 and digit > 7:
                    return 0
                answer = answer * 10 + digit
                x = x // 10
            return answer

        if x < 0:
            return -rev(abs(x))
        else:
            return rev(x)