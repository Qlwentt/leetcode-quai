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
            
        def isSorted(lst):
            for i in range(len(lst)-1):
                if lst[i] > lst[i+1]:
                    return False
            return True
        dfs(root)
        
        
        
        isSorted = isSorted(treeArray)
        noDup = len(treeArray) == len(set(treeArray))
        
        return isSorted and noDup