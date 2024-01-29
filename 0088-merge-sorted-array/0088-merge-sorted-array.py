class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
      #  [1,2,2,3,5,6] [2,5,6]
      #     P1        P2
      #             R
        
        
        P1 = m - 1
        P2 = n - 1
        
        for R in range(len(nums1)-1,-1,-1):
            num1 = nums1[P1] if P1 >= 0 else float('-inf')
            num2 = nums2[P2] if P2 >= 0 else float('-inf')
            if num1 > num2:
                nums1[R] = num1
                P1 -= 1
            else:
                nums1[R] = num2
                P2 -= 1
        
        