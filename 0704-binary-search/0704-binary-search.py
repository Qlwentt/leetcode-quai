class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0 
        hi = len(nums) -1
       # [-1,0,3,5,9,12]
        #  0 1 2 3 4 5
               

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
        return -1
    
# Time: O(log(N))
# Space: O(1)