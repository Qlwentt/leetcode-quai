from collections import defaultdict
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        answers = defaultdict(set)
        def backtrack(i, balance, curParens):
            if i == len(s):
                if balance == 0:
                    answers[len(curParens)].add("".join(curParens))
                return
            
            char = s[i]
            add = 0
            if char == "(":
                add = 1
            elif char == ")":
                add = -1
            balance += add
            
            if balance >= 0:
                curParens.append(char)
                backtrack(i+1, balance, curParens)
                curParens.pop()
                
            balance -= add
            backtrack(i+1, balance, curParens)
        backtrack(0, 0, [])
        maxLen = max(answers)
        return answers[maxLen]
            
                
        