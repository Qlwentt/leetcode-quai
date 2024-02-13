class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        remainder = 0
        answer = []
        while num1 or num2 or remainder:
            digit1 = int(num1.pop()) if num1 else 0
            digit2 = int(num2.pop()) if num2 else 0
            
            sum_ = digit1 + digit2 + remainder
            answer.append(str(sum_% 10))
            remainder = sum_ // 10
            
        answer.reverse()
        return "".join(answer)