from collections import defaultdict, deque
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(lambda: deque([]))
        
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                groups[r+c].appendleft(nums[r][c])
        
        answer = []
        for i in range(max(groups)+1):
            answer.extend(groups[i])
            
        return answer
            