# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not q or not p:
            return False
              
        leftsAreEqual = self.isSameTree(p.left,q.left)
        rightsAreEqual = self.isSameTree(p.right,q.right)
        
        return p.val == q.val and leftsAreEqual and rightsAreEqual
