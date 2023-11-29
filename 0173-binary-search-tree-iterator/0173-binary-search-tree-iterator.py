# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.nums.append(root.val)
            dfs(root.right)
        dfs(root)
        self.nxt = 0

    def next(self) -> int:
        answer = self.nums[self.nxt]
        self.nxt += 1
        return answer

    def hasNext(self) -> bool:
        return self.nxt in range(len(self.nums))



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()