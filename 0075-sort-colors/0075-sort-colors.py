class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
     #  [2,0,2,1,1,0]
     
        bucket = [0]*3
        
        for num in nums:
            bucket[num]+= 1
        #  [2,2,2]
        p = 0
       # [0,0,1,1,2,2]
        for i,amount in enumerate(bucket):
            for _ in range(amount):
                nums[p] = i
                p += 1
        
        
        