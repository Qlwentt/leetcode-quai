from bisect import bisect_left
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # [-4-1,1,2] target: 2
        #     [0]
        #  [0,1,3,6]
        nums.sort()
        print(nums)
        best = float('inf')
        for i in range(len(nums)):
            a = nums[i]
            new_target = target - a
            for j in range(i+1, len(nums)):
                b = nums[j]
                
                
                l = j + 1
                r = len(nums) -1
                                
                if l > r:
                    continue
                # [0, 3, 97, 102, 200]
                #     a  b   l     r
                while l < r:
                    mid = (l+r) // 2
                    if  (a+b+nums[mid]) - target > 0:
                        r = mid
                    elif (a+b+nums[mid]) - target < 0:
                        l = mid + 1
                    else:
                        l = mid
                        break
                
                closest = nums[l]
                best = min(best, a+b+closest, key= lambda x: abs(target-x))
                best = min(best, a+b+nums[l-1] if l-1 > j else float('inf'), key= lambda x: abs(target-x))
        return best
        
        
        