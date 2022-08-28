import re
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        s = re.split(r"(\+|\*|\-|\/)",s)
        stack = []
        operations = {
                "*": lambda a, b : a * b,
                "/": lambda a, b : int(a / b),
            }
        i = 0
        while i < len(s):
            curr = s[i]
            if curr.isdigit():
                stack.append(int(curr))
            elif curr == "-":
                stack.append(-int(s[i+1]))
                i += 2
                continue
            elif curr == "*" or curr == "/":
                stack[-1] = operations[curr](stack[-1],int(s[i+1]))
                i += 2
                continue
            i+=1
        return sum(stack)
                
            