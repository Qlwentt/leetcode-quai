from collections import deque
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        answer = []
        
        
        def dfs(row, col, forward, line):
            if (row not in range(ROWS) or 
                col not in range(COLS)):
                return line
            
            if forward:
                line.append(mat[row][col])
            else:
                line.appendleft(mat[row][col])
                
            a = dfs(row-1, col+1, forward, line)
            
            return a
        
        col = 0
        forward = True
        for row in range(ROWS):
            line = dfs(row,col, forward, deque([]))
            answer.extend(line)
            forward = not forward
        
        row = ROWS-1
        for col in range(1,COLS):
            line = dfs(row,col,forward,deque([]))
            answer.extend(line)
            forward = not forward
            
        return answer
            
            
        
        