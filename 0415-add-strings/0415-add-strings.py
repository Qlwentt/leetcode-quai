class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        num1 = list(num1)
        num2 = list(num2)
        answer = []
        while carry or num1 or num2:
            digit1 = int(num1.pop()) if num1 else 0
            digit2 = int(num2.pop()) if num2 else 0
            
            sum_ = digit1 + digit2 + carry
            answer.append(str(sum_ % 10))
            carry = sum_ // 10
        
        answer.reverse()
        return "".join(answer)
    
# O(max(N,M)) # worst case, iterate the longer of num1 and num2
# O(max(N,M)) # length of new string is max length of max string + 1