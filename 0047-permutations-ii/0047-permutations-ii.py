class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        def backtrack(curPerm, curNums):
            if len(curPerm) == len(nums) :
                answer.append(curPerm.copy())
                return
            
            for i in range(len(curNums)):
                if i == 0 or curNums[i-1] != curNums[i]:
                    curPerm.append(curNums[i])
                    backtrack(curPerm, curNums[:i] + curNums[i+1:])
                    curPerm.pop()
        backtrack([], nums)
        return answer
                