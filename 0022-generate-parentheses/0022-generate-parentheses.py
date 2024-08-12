class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers = []
        def backtrack(opens, closed, current):
            if opens == closed and opens == n:
                answers.append(current)
                return
            
            if opens < n:
                # can add opens
                backtrack(opens+1, closed, current+"(")
            
            if closed < opens:
                backtrack(opens, closed+1, current+")")
        backtrack(0,0,"")        
        return answers