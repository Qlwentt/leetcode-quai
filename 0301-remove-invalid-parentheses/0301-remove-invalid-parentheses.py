from collections import defaultdict
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        answer = defaultdict(set)
        
        def backtrack(i, curParens, curBalance):
            if i == len(s):
                if curBalance == 0:
                    answer[len(curParens)].add("".join(curParens))
                return
            
            char = s[i]
            add = 0
            if char == "(":
                add = 1
            elif char == ")":
                add = -1
            
            # take current char
            curParens.append(char)
            curBalance += add
            if curBalance >= 0:
                backtrack(i+1,curParens, curBalance)
            
                # skip current char
            curParens.pop()
            curBalance -= add
            if curBalance >= 0:
                backtrack(i+1, curParens, curBalance)
        backtrack(0, [], 0)
        maxKey = max(answer)
        return answer[maxKey]
        