class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        numsSet = set(nums)
        counts = collections.Counter(nums)
        answer = []
        for num in nums:
            if counts[num] == 1 and num + 1 not in numsSet and num - 1 not in numsSet:
                answer.append(num)
        return answer
        
        