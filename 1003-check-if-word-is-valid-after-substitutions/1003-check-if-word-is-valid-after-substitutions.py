class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == "c" and stack and stack[-1] == ['a','b']:
                stack.pop()
            else:
                if char == "a":
                    stack.append([char])
                else:
                    if stack:
                        stack[-1].append(char)
                    else:
                        return False
        return len(stack) == 0