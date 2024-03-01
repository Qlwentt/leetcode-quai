class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p3 = len(nums1) -1
        
        while p3 >= 0:
            val1 = nums1[p1] if p1 >= 0 else float('-inf')
            val2 = nums2[p2] if p2 >= 0 else float('-inf')
            
            if val1 > val2:
                nums1[p3] = val1
                p1 -= 1
            else:
                nums1[p3] = val2
                p2 -= 1
            p3 -= 1
        
        
                                        