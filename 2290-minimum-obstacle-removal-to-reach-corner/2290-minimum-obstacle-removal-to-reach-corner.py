class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        pq = []
        visited = {}
        ROWS = len(grid)
        COLS = len(grid[0])
        
        heapq.heappush(pq,(grid[0][0], 0, 0))
        
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        answer = float("inf")
        while pq:
            obstacles, r,c = heapq.heappop(pq)
            
            if (r,c) in visited and obstacles >= visited[(r,c)]:
                continue
            visited[(r,c)] = obstacles
            
            if (r,c) == (ROWS-1, COLS-1):
                return obstacles
                
            
            for dr, dc in directions:
                new_r, new_c = dr + r, dc + c
                if (
                    new_r in range(ROWS) and
                    new_c in range(COLS)
                ):
                    heapq.heappush(pq,(grid[new_r][new_c]+obstacles,new_r, new_c))
                    
        return answer       
            