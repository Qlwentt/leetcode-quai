class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minHeap = [(grid[0][0],0,0)]
        time = 0
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = set([(0,0)])
        
        while minHeap:
            curTime, row, col = heapq.heappop(minHeap)
            time = max(time, curTime)
            
            if (row,col) == (ROWS-1, COLS-1):
                return time
            
            for dr, dc in directions:
                r = dr + row
                c = dc + col
                if (r in range(ROWS) and c in range(COLS) and
                    (r,c) not in visited
                ):
                    heapq.heappush(minHeap, (grid[r][c], r,c))
                    visited.add((r,c))
        return time
                    
            
            
            
        