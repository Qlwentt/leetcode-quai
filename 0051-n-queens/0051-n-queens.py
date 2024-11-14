from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()
        answer = []
        def backtrack(r, cur_board):
            if len(cur_board) == n:
                answer.append(cur_board.copy())
                return

            line = ["."] * n
            for c in range(n):
                if c in cols or r+c in pos_diag or r-c in neg_diag:
                    continue
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                line[c] = "Q"
                
                cur_board.append("".join(line))
                backtrack(r+1, cur_board) 
                cur_board.pop()
                
                line[c] = "."
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
    
        backtrack(0,[])
        return answer
            
        