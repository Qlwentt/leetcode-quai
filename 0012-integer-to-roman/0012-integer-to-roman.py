class Solution:
    def intToRoman(self, num: int) -> str:
        convert = {1: "I", 5: "V", 10: "X",  50: "L", 100: "C",  500: "D", 1000: "M"}
        def toRoman(place, digit):
            if digit == 0:
                return ""
            if digit < 4: 
                return convert[place] * digit
            elif digit == 4 or digit == 9:
                return convert[place] + convert[(digit+1)*place]
            elif digit == 5:
                return convert[place*digit]
            else:
                return convert[place*5] + convert[place] * ((place*digit-place*5) // place)
                
        
        thousands = num // 1000
        num = num % 1000
        hundreds = num // 100
        num = num % 100
        tens = num // 10
        num = num % 10
        ones = num 
        
        return toRoman(1000, thousands) + toRoman(100, hundreds) + toRoman(10, tens) + toRoman(1, ones)
        
        