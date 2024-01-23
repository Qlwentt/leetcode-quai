import re
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s = re.split('(\-|\+|\*|\/)', s)
        operations = {
            "-" : lambda a: a * -1,
            "*" : lambda a,b: a * b,
            "/" : lambda a,b: int(a/b),
        }
        
        answer = 0
        a = 0
        i = 0
        while i < len(s):
            char = s[i]
            if char == "*":
                b = int(s[i+1])
                a = operations[char](a,b)
                i += 2
            elif char == "/":
                b = int(s[i+1])
                a = operations[char](a,b)
                i += 2            
            elif char == "-":
                b = int(s[i+1])
                answer += a
                a = operations[char](b)
                i += 2
            elif char == "+":
                b = int(s[i+1])
                answer += a
                a = b
                i += 2
            else:
                a = int(char)
                i += 1
        return answer + a