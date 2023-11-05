class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def backtrack(i, left):
            if i >= len(s):
                return left == 0
            if left < 0:
                return False
            if (i, left) in memo:
                return memo[(i,left)]
            
            if s[i] == "(":
                memo[(i,left)] = backtrack(i+1, left+1)
            elif s[i] == ")":
                memo[(i,left)] = backtrack(i+1, left-1)
            else:
                # left
                l = backtrack(i+1, left+1)
                # empty
                empty = backtrack(i+1, left)
                # right
                right = backtrack(i+1, left-1)
                memo[(i,left)] = l or empty or right
            return memo[(i,left)]
            
        return backtrack(0,0)