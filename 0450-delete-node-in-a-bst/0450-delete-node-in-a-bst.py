# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMin(root):
            current = root
            while current and current.left:
                current = current.left
            return current
        if not root:
            return root
        if root.val == key:
            # if one or zero children, return possibly present child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # else both children are present
            # replace root.val with val of inorder successor (minimum.val that is greater than val)
            # remove inorder successor
            inorderSuccessor = getMin(root.right)
            root.val = inorderSuccessor.val
            root.right = self.deleteNode(root.right, inorderSuccessor.val)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root