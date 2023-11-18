# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        coordinates = defaultdict(list)
        def dfs(root, row,col):
            if not root:
                return
            
            coordinates[(row,col)].append(root.val)
            # left
            dfs(root.left, row-1, col+1)
            # right
            dfs(root.right, row+1, col+1)
        dfs(root, 0,0)
        sortedCoordinates = list(coordinates.keys())
        sortedCoordinates.sort()
        answer = []
        
        prev = None 
        row = []
        i = 0
        while i < len(sortedCoordinates):
            if prev != None and prev != sortedCoordinates[i][0]:
                answer.append(row)
                row = []
            coord = sortedCoordinates[i]
            row.extend(coordinates[coord])
            prev = coord[0]
            i += 1
            
        answer.append(row)
        return answer
                
        