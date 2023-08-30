class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsSet = set(nums)
        answer =[]
        for i in range(1,len(nums)+1):
            if i not in numsSet:
                answer.append(i)
                
        return answer
            