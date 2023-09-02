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
                prev1 = stack.pop()
                prev2 = stack.pop()
                add_ = prev1 + prev2
                stack.extend([prev2,prev1,add_])
        return sum(stack)