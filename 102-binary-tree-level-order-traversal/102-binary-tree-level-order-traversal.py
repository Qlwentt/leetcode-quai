from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root,1)])
        result = []
        i = 1
        while q and q[0][0]:
            level = []
            while q and q[0][1] == i:
                node, j = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append((node.left, i+1))
                if node.right:
                    q.append((node.right, i+1))
            result.append(level)
            i+=1
        return result
            
            
                