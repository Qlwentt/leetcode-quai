class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        [1,2,3,0,0,0]
      #      I     P
        [2,5,6]
      #      J
    
        P = len(nums1) - 1
        i = m - 1
        j = n - 1
        
        while P >= 0:
            num1 = nums1[i] if i in range(len(nums1)) else float('-inf')
            num2 = nums2[j] if j in range(len(nums2)) else float('-inf')
            if num1 > num2:
                nums1[P], nums1[i] = nums1[i], nums1[P]
                i -= 1
            else:
                nums1[P], nums2[j] = nums2[j], nums1[P]
                j -= 1
            P -= 1
        