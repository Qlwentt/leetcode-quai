class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s = re.split(r'(\+|\-|\*|\/)', s)
        s = [item for item in s if item != ""]
        
        i = 0
        answer = 0
        stack = []
        while i < len(s):
            if s[i] == "+":
                answer += stack.pop()
                stack.append(int(s[i+1]))
                i += 2
            elif s[i] == "-":
                answer += stack.pop()
                stack.append(int(s[i+1]) * -1)
                i += 2
            elif s[i] == "*":
                a = stack.pop()
                b = int(s[i+1])
                stack.append(a*b)
                i += 2
            elif s[i] == "/":
                a = stack.pop()
                b = int(s[i+1])
                stack.append(int(a/b))
                i += 2
            else:
                stack.append(int(s[i]))
                i += 1
                
        if stack:
            answer += stack.pop()
            
        return answer