class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowsDict = collections.defaultdict(int)
        colsDict = collections.defaultdict(int)
        
        N = len(grid)
        
        for r in range(N):
            key = []
            for c in range(N):
                key.append(grid[r][c])
            rowsDict[tuple(key)] += 1
        
        for c in range(N):
            key = []
            for r in range(N):
                key.append(grid[r][c])
            colsDict[tuple(key)] += 1
        
        answer = 0    
        for key, count in rowsDict.items():
            if key in colsDict:
                answer += rowsDict[key] * colsDict[key]
        return answer