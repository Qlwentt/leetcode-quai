class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p1 = m - 1
        p2 = n - 1
        
        for i in range(len(nums1)-1,-1,-1):
            num1 = nums1[p1] if p1 >= 0 else float('-inf')
            num2 = nums2[p2] if p2 >= 0 else float('-inf')
            if num1 > num2:
                nums1[i] = num1
                p1 -= 1
            else:
                nums1[i] = num2
                p2 -= 1
        
        