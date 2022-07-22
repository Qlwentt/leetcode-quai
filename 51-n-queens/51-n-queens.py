class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        
        
        validBoards = []
        board = []
        
        rowTally = [False] * n
        colTally = [False] * n
        xDiagTally = [False] * (((n-1) * 2) +1)
        yDiagTally = [False] * (((n-1) * 2 )+1)
        
        def backtrack(possibleChoices):
            if not possibleChoices:
                validBoards.append(board[:])
                return
            
            for i, queenPosition in enumerate(possibleChoices):
                r = queenPosition
                c = len(board)
                
                if (rowTally[r] or
                    colTally[c] or 
                    xDiagTally[r-c + n - 1] or
                    yDiagTally[r+c]):
                    continue
                
                row = ["."] * n
                row[queenPosition] = "Q"
                row = "".join(row)
                board.append(row)
                
                rowTally[r] = True
                colTally[c] = True
                xDiagTally[r-c + n - 1] = True
                yDiagTally[r+c] = True
                
                backtrack(possibleChoices[:i]+possibleChoices[i+1:])
                
                board.pop()
                rowTally[r] = False
                colTally[c] = False
                xDiagTally[r-c + n - 1] = False
                yDiagTally[r+c] = False
            
        backtrack([i for i in range(n)])
        return validBoards
                
                    
        
            