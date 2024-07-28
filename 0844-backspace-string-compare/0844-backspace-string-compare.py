class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def write(word):
            stack = []
            for char in word:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        
        return write(s) == write(t)