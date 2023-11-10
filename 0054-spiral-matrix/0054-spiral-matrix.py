class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        ROWS = len(matrix)
        COLS = len(matrix[0])
        answer = []
        def spiral(row, col, prevRow, prevCol, direction):
            if (
                row not in range(ROWS) or
                col not in range(COLS) or
                (row,col) in visited
            ):
                return (prevRow, prevCol)
            
            answer.append(matrix[row][col])
            visited.add((row,col))
            
            if direction == "up":
                prev = spiral(row-1, col, row, col, "up")
            elif direction == "down":
                prev = spiral(row+1,col, row, col, "down")
            elif direction == "left":
                prev = spiral(row, col-1, row, col, "left")
            else:
                prev = spiral(row, col+1, row, col, "right")
            return prev                   
        
        row, col = 0, 0
        answer.append(matrix[row][col])
        visited.add((row,col))
        
        while len(visited) != len(matrix) * len(matrix[0]):
            row, col = spiral(row,col+1,row,col, "right")
            row, col = spiral(row+1, col, row, col, "down")
            row, col = spiral(row, col-1, row, col, "left")
            row, col = spiral(row-1, col, row, col, "up")
            
        return answer