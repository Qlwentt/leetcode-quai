class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
    #      1   11
    #     123  456
    #     456  123
    #     ---  ---
    #     738  368
    #  # 6150
    # # 49200
    # -------
   #    56088

        
        num1 = list(num1)
        num2 = list(num2)
        num1.reverse()
        num2.reverse()
        if len(num2) <= len(num1):
            num1, num2 = num2, num1
        answer = 0

        for i, digit1 in enumerate(num1):
            place = 10 ** i
            carry = 0
            for digit2 in num2:
                prod = (int(digit1) * int(digit2)) + carry
                answer += (prod % 10) * place
                carry = prod // 10
                place = place * 10
            answer += carry * place
            
        return str(answer)
            
            
            
        
        
         