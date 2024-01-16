class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        [0,1,3,0,4,2,2,2]
      #            P
      #.             Q
        
        P = 0
        Q = 0
        
        while Q < len(nums):
            if nums[Q] != val:
                nums[P], nums[Q] = nums[Q], nums[P]
                P += 1
                Q += 1
            else:
                Q += 1
                
        return P
            