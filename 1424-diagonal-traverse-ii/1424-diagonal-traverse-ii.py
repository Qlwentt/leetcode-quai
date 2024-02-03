from collections import defaultdict, deque
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(lambda: deque([]))
        ROWS = len(nums)
        for r in range(ROWS):
            for c in range(len(nums[r])):
                groups[r+c].appendleft(nums[r][c])
                
        i = 0
        answer = []
        while i in groups:
            answer.extend(groups[i])
            i += 1
        
        return answer
            
# Time: O(N) N is number of numbers in nums
# Space: O(N)