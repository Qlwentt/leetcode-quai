class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        answer = 0
        for r in range(len(grid)):
            max_col = float('-inf')
            max_row = float('-inf')
            for c in range(len(grid[0])):
                answer += grid[r][c] != 0
                max_col = max(grid[r][c], max_col)
                max_row = max(grid[c][r], max_row)
            
            answer += max_col
            answer += max_row
        return answer
        
        