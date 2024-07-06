class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        def altgroups(nums):
            prev = None
            streak = 1
            groups = 0
            for num in nums:
                if prev != None and prev != num:
                    streak += 1
                    if streak >= k:
                        groups += 1
                else:
                    streak = 1
                prev = num     
            return groups
        return altgroups(colors + colors[:(k-1)])
        