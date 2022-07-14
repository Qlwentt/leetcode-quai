from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        levelAnswer = deque([])
        
        if not root:
            return result
        
        q = deque([(root, 1)])
        forward = True
        level = 1
        while q:
            while q and q[0][1] == level:
                node, j = q.popleft()

                if forward:
                    levelAnswer.append(node.val)
                else:
                    levelAnswer.appendleft(node.val)

                if node.left:
                    q.append((node.left, j + 1))

                if node.right:
                    q.append((node.right, j + 1))
            
            result.append(levelAnswer)
            forward = not forward
            levelAnswer = deque([])
            level += 1
            
            
        return result

            
        