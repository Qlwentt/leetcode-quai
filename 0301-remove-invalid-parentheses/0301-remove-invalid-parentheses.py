class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        s = list(s)
        answers = defaultdict(set)
        def backtrack(i, curParens, balance):
            if i >= len(s):
                if balance == 0:
                    answers[len(curParens)].add("".join(curParens))
                return
                    
            # include
            curParens.append(s[i])
            add = 0
            if s[i] == "(":
                add = 1
            elif s[i] == ")":
                add = -1
            balance += add
            if balance >= 0:
                backtrack(i+1, curParens, balance)
                        
            # skip
            curParens.pop()
            balance -= add
            if balance >= 0:
                backtrack(i+1, curParens, balance)
        backtrack(0, [], 0) 
        maxLen = max(answers)
        return answers[maxLen]