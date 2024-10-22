# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make_tree(L,R):
            if L > R:
                return
            mid = (L + R) // 2
            root = TreeNode(nums[mid])
            root.left = make_tree(L,mid-1)
            root.right = make_tree(mid+1,R)
            return root
        return make_tree(0, len(nums)-1)
# Time: O(N)
# Space: O(log(N)) because the tree is balanced