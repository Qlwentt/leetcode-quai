from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsSet = defaultdict(set)
        colsSet = defaultdict(set)
        boxSet = defaultdict(set)
        
        ROWS = len(board)
        COLS = len(board[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                num = board[r][c]
                if num == ".":
                    continue
                
                if (num in rowsSet[r] or
                    num in colsSet[c] or
                    num in boxSet[(r//3, c//3)]):
                    return False
                
                rowsSet[r].add(num)
                colsSet[c].add(num)
                boxSet[(r//3, c//3)].add(num)
        return True
                    
                    
                    
                    
                
                