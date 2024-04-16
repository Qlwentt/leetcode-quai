from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        answerRight = []
        answerLeft = []
        while q:
            
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i == length - 1:
                    answerRight.append(node.val)
                if i == 0:
                    answerLeft.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        answerLeft.reverse()
        print(answerLeft)
        return answerRight
            
        