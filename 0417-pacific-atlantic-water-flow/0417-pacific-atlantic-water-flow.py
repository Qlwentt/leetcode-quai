class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reachPacific = set()
        reachAtlantic = set()
        
        ROWS = len(heights)
        COLS = len(heights[0])
        
        def dfs(row,col, visited, prev):
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                (row,col) in visited or
                heights[row][col] < prev
            ):
                return
            
            visited.add((row,col))
            cur = heights[row][col]
            
            dfs(row-1, col, visited, cur)
            dfs(row+1, col, visited, cur)
            dfs(row, col-1, visited, cur)
            dfs(row, col+1, visited, cur)
            return
            
            
            
        for col in range(COLS):    
            dfs(0,col,reachPacific,heights[0][col])
            dfs(ROWS-1,col,reachAtlantic,heights[ROWS-1][col])
               
        for row in range(ROWS):    
            dfs(row,0,reachPacific,heights[row][0])
            dfs(row,COLS-1,reachAtlantic,heights[row][COLS-1])
            
        
        answer = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) in reachPacific and (row,col) in reachAtlantic:
                    answer.append((row,col))
        return answer
            
            
            
            
                
            
        