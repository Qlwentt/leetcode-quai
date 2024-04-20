from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(lambda: deque([]))
        maxGroup = 0
        ROWS = len(nums)
        for r in range(ROWS):
            for c in range(len(nums[r])):
                groups[r+c].appendleft(nums[r][c])
                maxGroup = max(r+c, maxGroup)
        answer = []
        for i in range(maxGroup+1):
            answer.extend(groups[i])
        return answer
        