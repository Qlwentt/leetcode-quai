class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for char in s:
            top = stack[-1] if stack else ""
            if char in parens:
                stack.append(char)
            elif char == parens.get(top, None):
                stack.pop()
            else:
                return False
        return len(stack) == 0
        