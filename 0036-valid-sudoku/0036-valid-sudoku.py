from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num == ".":
                    continue
                if (num in rowSet[row] or
                    num in colSet[col] or
                    num in boxSet[(row//3, col//3)]):
                    return False
                rowSet[row].add(num)
                colSet[col].add(num)
                boxSet[(row//3, col//3)].add(num)
                
        return True