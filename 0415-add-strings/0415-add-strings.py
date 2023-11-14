class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        num1 = list(num1)
        num2 = list(num2)
        answer = []
        power = 0
        while num1 or num2 or carry:
            digit1 = int(num1.pop()) if num1 else 0
            digit2 = int(num2.pop()) if num2 else 0
            
            sum_ = digit1 + digit2 + carry
            answer.append(str(sum_ % 10)) 
        
            carry = sum_ // 10
        answer.reverse()
        return "".join(answer)