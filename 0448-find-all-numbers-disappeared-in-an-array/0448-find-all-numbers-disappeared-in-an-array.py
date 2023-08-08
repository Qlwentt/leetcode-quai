from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = {num:0 for num in range(1,len(nums)+1)}
        
        answer = []
        for num in nums:
            counter[num] += 1        
        
        for num, count in counter.items():
            if count == 0:
                answer.append(num)
                
        return answer
            