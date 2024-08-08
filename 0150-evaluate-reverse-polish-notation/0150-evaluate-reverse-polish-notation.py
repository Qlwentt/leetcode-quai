class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+": lambda a,b: a+b, "-": lambda a,b: a-b, "*": lambda a,b: a * b, "/": lambda a,b: int(a/b)}
        
        for char in tokens:
            if char in "+-*/":
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[char](a,b))
            else:
                stack.append(int(char))
        
        return stack[-1]