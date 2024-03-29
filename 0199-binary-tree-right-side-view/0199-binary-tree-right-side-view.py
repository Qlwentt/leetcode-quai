# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        answer = []
        q = deque([root])
        
        while q:
            haveAppended = False
            for _ in range(len(q)):
                node = q.popleft()
                if not haveAppended:
                    answer.append(node.val)
                    haveAppended = True
                    
                if node.right:
                    q.append(node.right)
                    
                if node.left:
                    q.append(node.left)
        
        return answer
                    