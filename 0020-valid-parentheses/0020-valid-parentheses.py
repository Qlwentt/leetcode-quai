class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        
        for char in s:
            if char in parens:
                stack.append(char)
            elif stack and parens[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return len(stack) == 0