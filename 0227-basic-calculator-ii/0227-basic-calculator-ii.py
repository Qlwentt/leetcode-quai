import re
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s = re.split(r'(\d*)', s)
        s = [item for item in s if item != ""]
        
        answer = 0
        i = 0
        stack = []
        while i < len(s):
            item = s[i]
            if item == "+":
                answer += stack.pop()
                stack.append(int(s[i+1]))
                i += 2
            elif item == "-":
                answer += stack.pop()
                stack.append(int(s[i+1])*-1)
                i += 2
            elif item == "*":
                a = stack.pop()
                b = int(s[i+1])
                stack.append(a*b)
                i += 2
            elif item == "/":
                a = stack.pop()
                b = int(s[i+1])
                stack.append(int(a/b))
                i += 2
            else:
                stack.append(int(item))
                i += 1
        
        if stack:
            answer += stack.pop()
            
        return answer
                
                
        