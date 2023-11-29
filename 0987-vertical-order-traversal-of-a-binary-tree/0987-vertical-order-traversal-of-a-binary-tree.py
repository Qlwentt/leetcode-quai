# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
import bisect
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        coordinates = defaultdict(list)
        
        def dfs(root, row,col):
            if not root:
                return
            
            bisect.insort(coordinates[col], (row, root.val))
            
            dfs(root.left, row+1, col-1)
            dfs(root.right,row+1,col+1)
        dfs(root, 0,0)
        cols = list(coordinates.keys())
        cols.sort()
        answer = []
        for col in range(cols[0], cols[-1]+1):
            answer.append([val for row, val in coordinates[col]])
        return answer
        
            
            
        
        
        
            