class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        answer = []
        
        def backtrack(i, curExpression):
            if i == len(num):
                curExpression = "".join(curExpression)
                if eval(curExpression) == target:
                    answer.append(curExpression)
                return
               
            operators = '+-*'
            for operator in operators:
                curExpression.append(operator)
                curExpression.append(num[i])
                backtrack(i+1, curExpression)
                curExpression.pop()
                curExpression.pop()
            if curExpression[-1].isdigit() and int(curExpression[-1]) != 0:
                updated = curExpression.copy()
                updated[-1] += num[i]
                backtrack(i+1, updated)
        backtrack(1, [num[0]])
        return answer
                