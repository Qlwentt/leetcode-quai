class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        answer = set([i for i in range(1,n+1)])
        
        for num in nums:
            if num in answer:
                answer.remove(num)
                
        return answer
            