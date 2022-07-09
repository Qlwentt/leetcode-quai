# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        treeArray = []
        def dfs(root):
            if not root:
                return treeArray
            dfs(root.left)
            if root:
                treeArray.append(root.val)
            dfs(root.right)
        dfs(root)
        
        isSorted = treeArray == sorted(treeArray)
        noDup = len(treeArray) == len(set(treeArray))
        
        return isSorted and noDup