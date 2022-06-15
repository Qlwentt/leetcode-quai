from typing import List

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) # key = (row, col) of the subbox
        
        n = 9
        
        for r in range(n):
            for c in range(n):
                ele = board[r][c]
                if ele == ".":
                    continue
                    
                if ele in rows[r] or ele in cols[c] or ele in boxes[(r//3, c//3)]:
                    return False
                rows[r].add(ele)
                cols[c].add(ele)
                boxes[(r//3, c //3)].add(ele)
        return True
# O(n^2) time
# O(n^2) space