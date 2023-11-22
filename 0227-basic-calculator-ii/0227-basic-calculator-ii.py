import re
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s = re.split('(\-|\+|\*|\/)', s)
        stack = []
        operations = {
            "-" : lambda a: a * -1,
            "*" : lambda a,b: a * b,
            "/" : lambda a,b: int(a/b),
        }
    
        i = 0
        while i < len(s):
            char = s[i]
            if char == "*":
                a = stack.pop()
                b = int(s[i+1])
                stack.append(operations[char](a,b))
                i += 2
            elif char == "/":
                a = stack.pop()
                b = int(s[i+1])
                stack.append(operations[char](a,b))
                i += 2            
            elif char == "-":
                a = int(s[i+1])
                stack.append(operations[char](a))
                i += 2
            elif char == "+":
                i += 1
            else:
                stack.append(int(char))
                i += 1
            
        return sum(stack)