# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversal = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            traversal.append(root.val)
            inorder(root.right)
        
        def isSorted(arr):
            for i in range(len(arr) - 1):
                if not arr[i] < arr[i+1]:
                    return False
            return True    
        inorder(root)
        return isSorted(traversal)
        
        