class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        answer = []
        def dfs(r,c,isForward):
            if (r not in range(ROWS) or
                c not in range(COLS)
            ):
                prevRow = r + 1 if isForward else r - 1
                prevCol = c - 1 if isForward else c + 1
                return (prevRow, prevCol)
            
            answer.append(mat[r][c])
            
            if isForward:
                return dfs(r-1,c+1, True)
            else:
                return dfs(r+1,c-1, False)
            
        
        r = 0
        c = 0
        
        while r in range(ROWS) and c in range(COLS):
            r, c = dfs(r,c, True)
            if c + 1 in range(COLS): # if can go right, do it, otherwise go down
                c += 1
            else:
                r += 1
            r, c = dfs(r,c, False)
            if r + 1 in range(ROWS): # if can go down do it, otherwise go right
                r += 1
            else:
                c += 1
        
        
        return answer        
                