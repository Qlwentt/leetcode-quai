class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        types = {
            "(":")",
            "{": "}",
            "[": "]",
        }
        for char in s:
            if char in types:
                stack.append(char)
            else:
                if not stack:
                    return False
                if types[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
    
# Time: O(N)
# Space: O(N)