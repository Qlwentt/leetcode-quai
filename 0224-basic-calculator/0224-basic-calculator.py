class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
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
                if stack and stack[-1] == "-":
                    stack.pop()
                    stack.append(current*-1)
                else:
                    stack.append(current)
                i += 1
            elif item.isdigit():
                stack.append(int(item))
                i += 1
            elif item == "(":
                stack.append(item)
                i += 1
            elif item == "-":
                if i+1 < len(s) and s[i+1].isdigit():
                    stack.append(int(s[i+1]) * -1)
                    i += 2
                else:
                    stack.append(item)
                    i += 1
            else:
                i += 1
        return sum(stack)
            