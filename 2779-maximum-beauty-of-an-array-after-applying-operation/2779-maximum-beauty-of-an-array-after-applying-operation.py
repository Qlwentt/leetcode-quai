class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        times = []
        
        for num in nums:
            times.append((num-k, 1))
            times.append((num+k+1, -1))
        times.sort()
        
        max_overlapping = 1
        cur_overlapping = 0
        for time, incrementer in times:
            cur_overlapping += incrementer
            max_overlapping = max(cur_overlapping, max_overlapping)
        
        return max_overlapping
        
        