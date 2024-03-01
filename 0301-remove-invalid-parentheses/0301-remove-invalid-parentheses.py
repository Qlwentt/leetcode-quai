from collections import defaultdict
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        answers = defaultdict(set)
        
        def backtrack(i, curParens, balance):
            if i == len(s):
                if balance == 0:
                    answers[len(curParens)].add("".join(curParens))
                return
            
            char = s[i]
            incr = 0
            
            if char == "(":
                incr = 1
            elif char == ")":
                incr = -1
                
            balance += incr
            
            if balance >= 0:
                curParens.append(char)
                backtrack(i+1, curParens, balance)
                curParens.pop()
                
            balance -= incr
            backtrack(i+1, curParens, balance)
        backtrack(0, [], 0)
        return answers[max(answers)] if len(answers) > 0 else []
            