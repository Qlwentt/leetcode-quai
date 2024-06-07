class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        rows_set = collections.defaultdict(int)
        cols_set = collections.defaultdict(int)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rows_set[r] += 1
                    cols_set[c] += 1
        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (rows_set[r] > 1 or cols_set[c] > 1):
                    answer += 1
        
        return answer
                    
        