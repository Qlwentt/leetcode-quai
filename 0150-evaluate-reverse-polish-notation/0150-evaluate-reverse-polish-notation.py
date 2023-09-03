class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ["2","1","+","3","*"]
        operations = {
            "+" : lambda a,b: a + b,
            "-" : lambda a,b: a - b,
            "*" : lambda a,b: a * b,
            "/" : lambda a,b: int(a/b)
        }
        stack = []
        for t in tokens:
            if t in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[t](a,b))
            else:
                stack.append(int(t))
        return stack[-1]