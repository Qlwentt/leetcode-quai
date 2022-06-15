from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paren if open < n
        # only add closed paren if closed < open
        # valid if closed == open == n
        
        result = []
       
        def backtrack(openN,closedN,parens):
            if openN == closedN == n:
                result.append(parens)
                return
            
            if openN < n:
                backtrack(openN+1,closedN,parens + "(")
                
            if closedN < openN:
                backtrack(openN, closedN+1, parens + ")")
            
        backtrack(0,0,"")
        return result