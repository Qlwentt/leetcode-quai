class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        nums = "".join([str(num) for num in nums])
        for i in range(len(nums)):
            num = int(nums[:i+1], 2)
            answer.append(num % 5 == 0)
            
        return answer