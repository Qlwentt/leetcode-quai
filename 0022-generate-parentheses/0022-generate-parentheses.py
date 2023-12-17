class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        def backtrack(stack, open_, closed):
            if open_ == closed == n:
                answer.append("".join(stack))
                return
            
            if open_ < n:
                stack.append("(")
                backtrack(stack, open_+1, closed)
                stack.pop()
            if closed < open_:
                stack.append(")")
                backtrack(stack, open_, closed+1)
                stack.pop()
        
        backtrack([], 0,0)
        return answer