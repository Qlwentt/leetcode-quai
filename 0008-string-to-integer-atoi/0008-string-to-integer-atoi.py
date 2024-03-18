class Solution:
    def myAtoi(self, s: str) -> int:
        isNegative = False
        s = s.strip()
        if s == "":
            return 0
        if s[0] == "-" or s[0] == "+":
            if s[0] == '-':
                isNegative = True
            s = s[1:]
          
        arr = list(s)
        arr.reverse()
        num = 0
        while arr and arr[-1].isnumeric():
            digit = arr.pop()
            num = (num * 10) + int(digit)
            
        
        answer =  num if not isNegative else -num
        
        if answer > 2 ** 31 -1:
            return 2 ** 31 -1
        elif answer < -2 ** 31:
            return -2 ** 31
        else:
            return answer
            
        