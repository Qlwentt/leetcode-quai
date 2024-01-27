class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        answer = []
        
        # returns last valid position of r and c
        def dfs(r,c, isForward):
            if (r not in range(ROWS) or
                c not in range(COLS)
               ):
                prevR = r + 1 if isForward else r - 1
                prevC = c - 1 if isForward else c + 1
                return (prevR, prevC)
            
            answer.append(mat[r][c])
            
            if isForward:
                # up and to the right
                prevR, prevC = dfs(r-1, c+1, True)
            else:
                # down and to the left
                prevR, prevC = dfs(r+1, c-1, False)
            
            return prevR, prevC
        
        r = 0
        c = 0
        
        while r in range(ROWS) and c in range(COLS):
            r, c = dfs(r,c,True) # go diagnally up until you can't anymore
            if c + 1 in range(COLS): # move right if you can otherwise move down
                c += 1
            else:
                r += 1
            r,c = dfs(r,c,False) # go diagonally down until you can't anymore
            if r + 1 in range(ROWS): # move down if you can, otherwise move right
                r += 1
            else:
                c += 1
        return answer