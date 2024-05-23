class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ROWS = numRows
        sections = ceil(len(s) / (2 * numRows - 2.0))
        COLS = sections * (numRows - 1)
        
        
        
        grid = [[""] * COLS for _ in range(ROWS)]
       
        r = 0
        c = 0
        i = 0
        visited = set()
        while i < len(s):
            while r in range(ROWS):
                if (r,c) not in visited and i < len(s):
                    grid[r][c] = s[i]
                    i += 1
                    visited.add((r,c))
                r += 1
            r -= 1
            while r in range(ROWS) and c in range(COLS):
                if (r,c) not in visited and i < len(s):
                    grid[r][c] = s[i]
                    i += 1
                    visited.add((r,c))
                r -= 1
                c += 1
            r += 1
            c -= 1
        answer = []
        
        for r in range(ROWS):
            for c in range(COLS):
                answer.append(grid[r][c])
                
        return "".join(answer)
            
            
            
        
        