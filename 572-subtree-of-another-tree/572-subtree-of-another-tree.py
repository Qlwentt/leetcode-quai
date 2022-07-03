# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p,q):
        if not p and not q:
            return True
        pVal = p.val if p else None
        qVal = q.val if q else None
        
        pleft, pRight = (p.left, p.right) if p else (None,None)
        qleft, qRight = (q.left, q.right) if q else (None,None)
        
        leftsAreEqual = self.isSameTree(pleft , qleft)
        rightsAreEqual = self.isSameTree(pRight, qRight)
        
        if pVal == qVal and leftsAreEqual and rightsAreEqual:
            return True
        return False
    