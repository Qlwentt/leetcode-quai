class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        carry = 0
        answer = []
        while num1 or num2 or carry:
            digit1 = int(num1.pop()) if num1 else 0
            digit2 = int(num2.pop()) if num2 else 0
            
            sum_ = digit1 + digit2 + carry
            ansDigit = sum_ % 10
            carry = sum_ // 10
            answer.append(str(ansDigit))
            
        answer.reverse()
        return "".join(answer)
            
        