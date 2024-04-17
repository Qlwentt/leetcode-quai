class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [1,2,3,0,0,0]
        #            P3
        p1 = m - 1
        p2 = n - 1
        p3 = len(nums1) - 1
        
        while p1 >= 0 or p2 >= 0:
            num1 = nums1[p1] if p1 >= 0 else float('-inf')
            num2 = nums2[p2] if p2 >= 0 else float('-inf')
            
            if num1 > num2:
                nums1[p1], nums1[p3] = nums1[p3], nums1[p1]
                p1 -= 1
            else:
                nums2[p2], nums1[p3] = nums1[p3], nums2[p2]
                p2 -= 1
            p3 -= 1
        