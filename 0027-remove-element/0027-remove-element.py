class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [3,3,2,3] 3
        #  L
        #      R
        # [2,3,3,3]

        # [0,1,3,0,4,2,2,2] 2 
        #            k        
        #                  i
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
  
        