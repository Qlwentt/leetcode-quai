class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # [3,6,1,2,5]
        #[1, 2, 3, 5, 6] 
        nums.sort()
        cur_min = float('inf')
        num_subsequences = 1
        for num in nums:
            possible_min = min(cur_min, num)
            if num - possible_min <= k:
                cur_min = possible_min
            else:
                num_subsequences += 1
                cur_min = num
        return num_subsequences
        