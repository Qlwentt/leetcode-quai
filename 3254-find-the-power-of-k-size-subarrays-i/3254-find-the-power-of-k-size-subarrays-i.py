class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
      # [1,2,3,4,3,2,5]
      #  T T T
        # [3,2,3,2,3,2]
        #  T F T
        # 2
    
        l = 0
        answer = []
        def is_sorted(arr):
            prev = arr[0] - 1
            for num in arr:
                if prev + 1 != num:
                    return False
                prev = num
            return True
        for r in range(len(nums)):
            if r-l+1 == k:
                answer.append(nums[r] if is_sorted(nums[l:l+k])  else -1)
                l += 1
        return answer