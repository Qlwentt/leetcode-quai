class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        minHeap = [(grid[0][0],0,0)]
        visited = set()
        
        while True:
            maxHeight, r, c = heapq.heappop(minHeap)
            if r == n - 1 and c == n - 1:
                return maxHeight
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for r2, c2 in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if (r2 < 0 or c2 < 0 or
                    r2 >= n or c2 >= n
                ):
                    continue
                heapq.heappush(minHeap, (max(maxHeight, grid[r2][c2]), r2,c2))
        
            