class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = {}
        def count(r,c):
            if (r not in range(ROWS) or 
                c not in range(COLS)):
                return 0
            if matrix[r][c] == 0:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            right = count(r, c+1)
            diag = count(r+1,c+1)
            down = count(r+1,c)
            
            ans = min(right, diag,down) + 1
            cache[(r,c)] = ans
            return ans
        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                answer += count(r,c)
                
        return answer
            
            
            