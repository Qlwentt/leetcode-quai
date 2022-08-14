class Solution:
    def reverse(self, x: int) -> int:
        maxInt = 2 ** 31 -1
        isNeg = x < 0
        x = abs(x)
        reverse = 0
        while x:
            digit = x % 10
           
            if ((reverse > maxInt // 10) 
                or ((reverse  == maxInt // 10) and digit > maxInt % 10)):
                return 0
            reverse = reverse * 10 + digit
            x = x // 10
        return reverse if not isNeg else -reverse