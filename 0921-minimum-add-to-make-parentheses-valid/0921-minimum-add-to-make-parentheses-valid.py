class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        add = 0
        
        for char in s:
            if char == "(":
                stack.append("(")
            else: # char == )
                if stack:
                    stack.pop()
                else:
                    add += 1
                
        
        return add + len(stack)
    
# Time: O(N) iterate through string once
# Space O(1) only use int vars