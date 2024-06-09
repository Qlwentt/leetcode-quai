class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        curr = 0 
        for num in nums:
            curr += num
            answer.append(curr % 5 == 0)
            curr = curr * 2
        return answer