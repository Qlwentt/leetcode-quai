class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        powersOfTen = { 100: "Hundred", 1000: "Thousand", 1*10**6: "Million", 1*10**9:"Billion" }
        numToWords = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16:"Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        if num in numToWords:
            return numToWords[num]
        # 2147483647
        def convert(num, place):
            if num == 0:
                return ""
            if place == 10 or place == 1:
                return numToWords[num*place]
            elif num not in numToWords:
                return self.numberToWords(num) + " " + powersOfTen[place]
                # hundreds = num(num // 100, 100)
                # num = num % 100
                # tens = convert(num // 10, 10)
                # num = num % 10
                # ones = convert(num, 1)
                # return " ".join(filter(None, [hundreds, tens, ones, powersOfTen[place]]))
            else:
                return numToWords[num] + " "+ powersOfTen[place]
        
        
        billions = num // (1*10**9)
        num = num % (1*10**9)
        
        millions = num // (1*10**6)
        num = num % (1*10**6)
        
        thousands = num // 1000
        num = num % 1000
        
        hundreds = num // 100
        num = num % 100
        
        override = None
        if num in numToWords:
            override = numToWords[num]
        
        tens = num // 10
        num = num % 10
        
        ones = num
        
        answer = [convert(billions, 1*10**9), convert(millions, 1*10**6), convert(thousands, 1000), convert(hundreds, 100), convert(tens, 10) if not override else override, convert(ones, 1) if not override else ""]
        return " ".join(filter(None, answer))
        
        
        