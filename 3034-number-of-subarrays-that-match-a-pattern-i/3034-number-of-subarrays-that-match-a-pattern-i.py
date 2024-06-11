from operator import gt, lt, eq
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        count = 0
        operator = {1:gt, 0:eq, -1:lt}
        for i in range(len(nums)):
            sub_array = []
            j = i
            match = True
            k = 0
            while i + len(pattern) < len(nums) and j < i+len(pattern)+1:
                if sub_array:
                    if not operator[pattern[k]](nums[j],sub_array[-1]):
                        match = False
                        break
                    k += 1
                sub_array.append(nums[j])
                j += 1
            count += match and len(sub_array) > 0
        return count
            
        
        
       