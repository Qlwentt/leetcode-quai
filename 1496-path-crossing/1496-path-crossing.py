class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0,0)])
        row, col = 0, 0
        
        for direction in path:
            if direction == "N":
                row -= 1
            elif direction == "S":
                row += 1
            elif direction == "E":
                col += 1
            else:
                col -= 1
            if (row,col) in visited:
                return True
            visited.add((row,col))
        return False