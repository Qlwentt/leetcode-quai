class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prev = 0
        nums.append(10**9+1)
        start = end = kstart = kend = 0
        for i in range(len(nums)-1):
            num = nums[i]
            if nums[i+1] != num + 1:
                start = num+1
                end = nums[i+1]-1
                kstart = prev+1
                kend = kstart + (end - start)
                prev = kend
                if k in range(kstart, kend+1):
                    return start + (k - kstart)
            
        