class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#         [1,2,2,3,5,6] [0,0,0]
#         [1,2,3,4,5,5] [0,0,0]
        
#         [1,2,3,0,5,6] [2,0,0]
      #        L            
      #          R
      #                  l
    
        
        L1 = m - 1
        L2 = n - 1
        R = len(nums1) - 1
        
        while R > L1:
            num1 = nums1[L1] if L1 >= 0 else float('-inf')
            num2 = nums2[L2] if L2 >= 0 else float('-inf')            
            
            if num1 > num2:
                nums1[L1], nums1[R] = nums1[R], nums1[L1]
                L1 -= 1
            else:
                nums2[L2], nums1[R] = nums1[R], nums2[L2]
                L2 -= 1
            R -= 1
            
        
        
            