class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        pairs = {}
        for one in nums1:
            for two in nums2:
                pairs[one+two] = pairs.get(one+two, 0) + 1
        count = 0
        for three in nums3:
            for four in nums4:
                if -(three+four) in pairs:
                    count += pairs[-(three+four)]
        return count