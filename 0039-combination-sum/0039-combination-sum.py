class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # combs = []
        nums = candidates

#         def backtrack(i, curComb, curSum):
#             if curSum == target:
#                 combs.append(curComb.copy())
#                 return
            
#             if i >= len(nums) or curSum > target:
#                 return
            
#             # choose num between 1 and unlimited times
#             curComb.append(nums[i])
#             backtrack(i, curComb, curSum + nums[i])
            
#             # skip num
#             curComb.pop()
#             backtrack(i+1, curComb, curSum)
        
#         backtrack(0, [], 0)
#         return combs
# Time: O(2^T*N) where T is the target value and N is the number of candidates
# Space: O(T) where T is the target value
        
        combs = set()
        def backtrack(i, cur_comb, cur_sum):
            if cur_sum > target:
                return
            if cur_sum == target:
                combs.add(tuple(sorted(cur_comb)))
            for j in range(i, len(nums)):
                cur_comb.append(nums[j])
                backtrack(j, cur_comb, cur_sum+ nums[j])
                cur_comb.pop()
        backtrack(0,[], 0)
        return list(combs)
        
        