class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        visiting = set()
        
        def backtrack(row,col, i):
            if (i == len(word)):
                return True
            
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                (row,col) in visiting or 
                board[row][col] != word[i]
            ):
                return False
            
            visiting.add((row,col))
            
            up = backtrack(row-1, col, i+1)
            down = backtrack(row+1, col, i+1)
            left = backtrack(row, col-1, i+1)
            right = backtrack(row, col+1, i+1)
            
            visiting.remove((row,col))
            
            return up or down or left or right
        
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row,col, 0):
                    return True
                
        return False
        
                
        
        