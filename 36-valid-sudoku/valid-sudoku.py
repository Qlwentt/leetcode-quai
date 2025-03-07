from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows_dict = defaultdict(set)
        # cols_dict = defaultdict(set)
        # boxes_dict = defaultdict(set)
        
        # N = len(board)
        
        # for r in range(N):
        #     for c in range(N):
        #         num = board[r][c]
        #         if num == ".":
        #             continue
                
        #         if (num in rows_dict[r] or
        #             num in cols_dict[c] or
        #             num in boxes_dict[(r//3, c//3)]):
        #             return False
                
        #         rows_dict[r].add(num)
        #         cols_dict[c].add(num)
        #         boxes_dict[(r//3, c//3)].add(num)
        # return True

# Time: O(N^2)
# Space: O(N^2)
        N = len(board)
        for r in range(N):
            row_set = set()
            for c in range(N):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_set:
                    return False
                row_set.add(board[r][c])

        for r in range(N):
            col_set = set()
            for c in range(N):
                if board[c][r] == ".":
                    continue
                if board[c][r] in col_set:
                    return False
                col_set.add(board[c][r])
                
        for r_start in range(0,N,3):
            for c_start in range(0,N,3):
                box_set = set()
                for r in range(r_start, r_start+3):
                    for c in range(c_start, c_start+3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in box_set:
                            return False
                        box_set.add(board[r][c])
        return True

    # Time: O(N^2)
    # Space: O(N)
                    
                    
                    
                
                