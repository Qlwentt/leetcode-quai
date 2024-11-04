class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        
        def backtrack(i, cur_set):
            if i >= len(nums):
                power_set.append(cur_set.copy())
                return
            
            # choose number
            cur_set.append(nums[i])
            backtrack(i+1, cur_set)
            
            # skip number
            cur_set.pop()
            backtrack(i+1, cur_set)

        backtrack(0, [])
        return power_set
# Time: O(N*2^N)
# Space: O(N) (not counting output)