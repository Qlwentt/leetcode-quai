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
        
        pVal = p.val if p else None
        qVal = q.val if q else None
        
        leftP = p.left if p else None
        leftQ = q.left if q else None
        
        rightP = p.right if p else None
        rightQ = q.right if q else None
        
        
        leftsAreEqual = self.isSameTree(leftP,leftQ)
        rightsAreEqual = self.isSameTree(rightP,rightQ)
        
        return pVal == qVal and leftsAreEqual and rightsAreEqual
