class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3:
            return []
        nums.sort(reverse=True)
        answer = []
        a = []
        while nums:
            b = nums.pop()
            if not a or b - a[0] <= k:
                a.append(b)
                if len(a) == 3:
                    answer.append(a)
                    a = []
            else:
                return []
                
        return answer