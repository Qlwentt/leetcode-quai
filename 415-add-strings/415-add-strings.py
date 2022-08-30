class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        output = []
        power = 0
        carry = 0
        num1 = list(num1)
        num2 = list(num2)
        while num1 or num2 or carry:
            digit1 = int(num1.pop()) if num1 else 0
            digit2 = int(num2.pop()) if num2 else 0
            
            sumNum = digit1 + digit2 + carry
            sumDig = sumNum % 10
            carry = sumNum // 10
            output.append(str(sumDig))
        return "".join(output[::-1])