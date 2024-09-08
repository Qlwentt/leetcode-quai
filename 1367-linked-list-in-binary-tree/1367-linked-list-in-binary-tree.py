# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    
        def dfs(node, ll_node):
            if ll_node is None:
                return True
            if not node:
                return False
            
            if ll_node.val != node.val:
                return False
            
            return dfs(node.left, ll_node.next) or dfs(node.right,ll_node.next)
        
        if head == None:
            return True
        if root == None:
            return False
        
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right) 
    
            