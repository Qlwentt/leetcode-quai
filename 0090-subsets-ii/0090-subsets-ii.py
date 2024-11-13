class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        def backtrack(i, cur_set):
            if i == len(nums):
                answer.append(cur_set.copy())
                return
            
            # include between 1 and multiple of the number
            cur_set.append(nums[i])
            backtrack(i+1, cur_set)
            
            # do not include the number
            cur_set.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, cur_set)
        
        backtrack(0, [])
        return answer
    
# Time: O(N*2^N)
# Space: O(N)