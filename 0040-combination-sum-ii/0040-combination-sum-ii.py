class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        combs = []
        nums.sort()

        def backtrack(i, curComb, curSum):
            if curSum == target:
                combs.append(curComb.copy())
                return
            
            if i >= len(nums) or curSum > target:
                return
            
            # chose num between 1 and multiple times
            curComb.append(nums[i])
            backtrack(i+1, curComb, curSum + nums[i])
            
            curComb.pop()
            # skip num
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, curComb, curSum)
            
        backtrack(0, [], 0)
        return combs