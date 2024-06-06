class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        stack = list(t)
        stack.reverse()
        
        for char in s:
            if char == stack[-1]:
                stack.pop()
            if not stack:
                break
        return len(stack)