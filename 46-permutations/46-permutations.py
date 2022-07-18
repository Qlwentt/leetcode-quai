class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(currentNums, path):
            if not currentNums:
                res.append(path)
                return
            for i in range(len(currentNums)):
                backtrack(currentNums[:i]+currentNums[i+1:], path + [currentNums[i]])
        backtrack(nums, [])
        return res