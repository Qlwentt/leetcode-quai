class Solution:
    def calculate(self, s: str) -> int:
        s = re.split(r'(\d*)', s)
        s = [item for item in s if item != ""]
        
        stack = []
        
        i = 0
        
        while i < len(s):
            item = s[i]
            
            if item == ")":
                current = 0
                while stack and stack[-1] != "(":
                    current += stack.pop()
                if stack:
                    stack.pop()
                if stack and type(stack[-1]) is str and stack[-1] in "-*/":
                    operator = stack.pop()
                    if operator == "-":
                        stack.append(current*-1)
                    elif operator == "*":
                        a = stack.pop()
                        b = current
                        stack.append(a*b)
                    else:
                        a = stack.pop()
                        b = current
                        stack.append(int(a/b))
                else:
                    stack.append(current)
                i += 1
            elif item == "(":
                stack.append(item)
                i += 1
            elif item == "+":
                i += 1
            elif item == "-":
                if i + 1 < len(s) and s[i+1].isdigit():
                    stack.append(int(s[i+1])*-1)
                    i += 2
                else:
                    stack.append(item)
                    i += 1
            elif item == "*":
                if i + 1 < len(s) and s[i+1].isdigit():
                    a = stack.pop()
                    b = int(s[i+1])
                    stack.append(a*b)
                    i += 2
                else:
                    stack.append(item)
                    i += 1
            elif item == "/":
                if i + 1 < len(s) and s[i+1].isdigit():
                    a = stack.pop()
                    b = int(s[i+1])
                    stack.append(int(a/b))
                    i += 2
                else:
                    stack.append(item)
                    i += 1
            else:
                stack.append(int(item))
                i += 1
            
        return sum(stack)