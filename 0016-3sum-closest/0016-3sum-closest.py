from bisect import bisect_left
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # [-4-1,1,2] target: 2
        #     [0]
        #  [0,1,3,6]
        nums.sort()
        best = float('inf')
        for i in range(len(nums)):
            a = nums[i]
            new_target = target - a
            for j in range(i+1, len(nums)):
                b = nums[j]
                comp = new_target - b
                l = j+1
                r = len(nums) - 1
                
                while l <= r:
                    mid = (l+r) // 2
                    if nums[mid] >= comp:
                        r = mid - 1
                    else:
                        l = mid + 1
                leftmost = l
                best = min(best, a+b+ nums[leftmost-1] if leftmost - 1 > j  else float('inf'), key= lambda x: abs(x-target))     
                best = min(best, a+b+ nums[leftmost] if leftmost < len(nums) and leftmost > j else float('inf'), key= lambda x: abs(x-target))
                best = min(best, a+b+ nums[leftmost+1] if leftmost + 1 < len(nums) and leftmost+ 1 > j else float('inf') , key= lambda x: abs(x-target))
        return best
        
        
        