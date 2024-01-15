from collections import deque
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        ROWS = len(maze)
        COLS = len(maze[0])
        shortestPaths = defaultdict(lambda: float(inf))
        minHeap = [(0, start[0], start[1])]
     
        directions = [[0,1],[1,0],[0,-1], [-1,0]]
        while minHeap:
            length, r, c = heapq.heappop(minHeap)
            if [r,c] == destination:
                return length
            
            for dr, dc in directions:
                newR = r
                newC = c
                newLength = length

                while (newR+dr) in range(ROWS) and (newC+dc) in range(COLS) and maze[(newR+dr)][(newC+dc)]!= 1:
                    newR += dr
                    newC += dc
                    newLength += 1

                if newLength < shortestPaths[(newR,newC)]:
                    heapq.heappush(minHeap, (newLength, newR, newC))
                    shortestPaths[(newR,newC)] = newLength        
        
        return -1
        
        