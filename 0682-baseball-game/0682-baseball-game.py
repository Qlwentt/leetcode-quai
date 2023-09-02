class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if op.lstrip('-').isnumeric():
                stack.append(int(op))
            elif op == "C":
                stack.pop()
            elif op == "D":
                prev = stack[-1]
                stack.append(prev*2)
            elif op == "+":
                stack.append(stack[-1]+stack[-2])
        return sum(stack)