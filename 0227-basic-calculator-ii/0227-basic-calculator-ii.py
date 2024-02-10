class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s = re.split(r'(\+|\-|\*|\/)', s)
        s = [item for item in s if item != ""]

        i = 0
        stack = []
        answer = 0
        while i < len(s):
            char = s[i]
            if char.isnumeric():
                stack.append(int(char))
                i += 1
            elif char == "+":
                answer += stack.pop()
                i += 1
            elif char == "-":
                answer += stack.pop()
                stack.append(int(s[i+1]) * -1)
                i += 2
            elif char == "*":
                a = stack.pop()
                b = int(s[i+1])
                stack.append(a*b)
                i += 2
            elif char == "/":
                a = stack.pop()
                b = int(s[i+1])
                stack.append(int(a/b))
                i += 2
            
        if stack:
            answer += stack.pop()
            
        return answer
                