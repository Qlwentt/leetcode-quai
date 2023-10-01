class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        nums = candidates

        def backtrack(i, curComb, curSum):
            if curSum == target:
                combs.append(curComb.copy())
                return
            
            if i >= len(nums) or curSum > target:
                return
            
            # choose num between 1 and unlimited times
            curComb.append(nums[i])
            backtrack(i, curComb, curSum + nums[i])
            
            # skip num
            curComb.pop()
            backtrack(i+1, curComb, curSum)
        
        backtrack(0, [], 0)
        return combs