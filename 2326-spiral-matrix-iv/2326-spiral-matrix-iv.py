# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ROWS = m
        COLS = n
        
        grid = [[None] * COLS for _ in range(ROWS)] 
        r = 0
        c = 0
        current = head
        while r in range(ROWS) and c in range(COLS) and grid[r][c] == None:
            # right
            while c in range(COLS) and grid[r][c] == None:
                grid[r][c] = current.val if current else -1
                if current:
                    current = current.next
                c += 1
            r += 1
            c -= 1
            # down
            while r in range(ROWS) and grid[r][c] == None:
                print(r)
                grid[r][c] = current.val if current else -1
                if current:
                    current = current.next
                r += 1            
               
            # left
            r -= 1
            c -= 1
            while c in range(COLS) and grid[r][c] == None:
                grid[r][c] = current.val if current else -1
                if current:
                    current = current.next
                c -= 1
            
            r -= 1
            c += 1
            # up
            while r in range(ROWS) and grid[r][c] == None:
                grid[r][c] = current.val if current else -1
                if current:
                    current = current.next
                r -= 1
            c += 1
            r += 1
        return grid
            