class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        ROWS = len(matrix)
        COLS = len(matrix[0])
        answer = []
        directions = {
            "up": True,
            "down": True,
            "left": True,
            "right": True
        }
        def spiralOrder(row, col, d):
            if (
                row not in range(ROWS) or
                col not in range(COLS) or
                (row,col) in visited or
                not directions[d]
            ):
                return False
            
            answer.append(matrix[row][col])
            visited.add((row,col))
            
            # right
            while len(visited) != len(matrix) * len(matrix[0]):
                if not spiralOrder(row, col+1, "right"):
                    directions["right"] = False
                    # down
                    if not spiralOrder(row+1, col, "down"):
                        directions["down"] = False
                        #left
                        if not spiralOrder(row, col-1, "left"):
                            directions["left"] = False
                            # up
                            if not spiralOrder(row-1, col, "up"):
                                directions["up"] = True
                                directions["down"] = True
                                directions["left"] = True
                                directions["right"] = True
                                
            return True
            
        spiralOrder(0,0, "right")
        return answer