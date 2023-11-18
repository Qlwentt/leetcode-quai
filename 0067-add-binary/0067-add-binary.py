class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = list(a)
        b = list(b)
        answer = []
        while a or b or carry:
            aDigit = int(a.pop()) if a else 0
            bDigit = int(b.pop()) if b else 0
            sum_ = aDigit + bDigit + carry
            digit = sum_ % 2
            answer.append(str(digit))
            carry = sum_ // 2
        answer.reverse()
        return "".join(answer)
            