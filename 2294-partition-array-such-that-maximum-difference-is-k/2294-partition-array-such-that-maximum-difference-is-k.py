class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # [3,6,1,2,5]
        #[1, 2, 3, 5, 6] 
        nums.sort()
        cur_min = float('inf')
        cur_max = float('-inf')
        num_subsequences = 1
        for num in nums:
            possible_min = min(cur_min, num)
            possible_max = max(cur_max, num)
            if possible_max - possible_min <= k:
                cur_min = possible_min
                cur_max = possible_max
            else:
                num_subsequences += 1
                cur_min = num
                cur_max = num
        return num_subsequences
        