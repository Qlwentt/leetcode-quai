class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        for row in nums:
            row.sort(reverse=True)
        
        ROWS = len(nums)
        COLS = len(nums[0])
        score = 0
        for c in range(COLS):
            max_num = float('-inf')
            for r in range(ROWS):
                max_num = max(nums[r][c], max_num)
            score += max_num
        
        return score
                
            
        
        
        