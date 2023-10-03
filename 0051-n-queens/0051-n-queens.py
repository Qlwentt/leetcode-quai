from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = defaultdict(lambda: False)
        xdiag = defaultdict(lambda: False)
        ydiag = defaultdict(lambda: False)
        answer = []
        def backtrack(row, curBoard):
            if len(curBoard) == n:
                answer.append(curBoard.copy())
                return

            line = ["."] * n
            for c in range(n):
                if cols[c] or xdiag[c-row] or ydiag[c+row]:
                    continue
                cols[c] = True
                xdiag[c-row] = True
                ydiag[c+row] = True
                line[c] = "Q"
                
                curBoard.append("".join(line))
                backtrack(row+1, curBoard) 
                curBoard.pop()
                
                line[c] = "."
                cols[c] = False
                xdiag[c-row] = False
                ydiag[c+row] = False
    
        backtrack(0,[])
        return answer
            
        