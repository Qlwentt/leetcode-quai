class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def backtrack(i, curSubset):
            if i == len(nums):
                answer.append(curSubset.copy())
                return
            
            curSubset.append(nums[i])
            backtrack(i+1, curSubset)
            curSubset.pop()
            backtrack(i+1, curSubset)
        backtrack(0, [])
        return answer