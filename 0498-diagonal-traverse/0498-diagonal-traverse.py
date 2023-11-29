from collections import deque
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        ROWS = len(mat)
        COLS = len(mat[0])
        
        answer = []
        directions = {
            True: lambda row, col, fn: fn(row-1,col+1, True),
            False: lambda row, col, fn: fn(row+1,col-1, False),
        }
        
        def dfs(row, col, forward):
            if (row not in range(ROWS) or 
                col not in range(COLS)):
                prevRow = row + 1 if forward else row -1
                prevCol = col - 1 if forward else col + 1
                return prevRow, prevCol
                
            answer.append(mat[row][col])
            r, c = directions[forward](row, col, dfs)
            return r,c
        
        row = 0
        col = 0
        
        while row in range(ROWS) and col in range(COLS):
            row, col = dfs(row,col, True)
            if col + 1 in range(COLS):
                col += 1
            else:
                row += 1
            row, col = dfs(row,col,False)
            if row +1 in range(ROWS):
                row += 1
            else:
                col += 1
            
                
        return answer