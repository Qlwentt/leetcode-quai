class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # one-liner intersection of two sets
        return list(set(nums1) & set(nums2))

        # Time: O(min(n,m))
        # Space: O(n+m)



        # manually performing intersection of two sets
        set1 = set(nums1)
        set2 = set(nums2)

        # always ensure set 1 is smaller than set 2
        if len(set1) > len(set2):
            set1 , set2 = set2, set1

        return [num for num in set1 if num in set2]

        # Time: O(min(n,m))
        # Space: O(n+m)
        
