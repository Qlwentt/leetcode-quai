from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        boxes_dict = defaultdict(set)
        
        N = len(board)
        
        for r in range(N):
            for c in range(N):
                num = board[r][c]
                if num == ".":
                    continue
                
                if (num in rows_dict[r] or
                    num in cols_dict[c] or
                    num in boxes_dict[(r//3, c//3)]):
                    return False
                
                rows_dict[r].add(num)
                cols_dict[c].add(num)
                boxes_dict[(r//3, c//3)].add(num)
        return True

# Time: O(N^2)
# Space: O(N^2)
                    
                    
                    
                    
                
                