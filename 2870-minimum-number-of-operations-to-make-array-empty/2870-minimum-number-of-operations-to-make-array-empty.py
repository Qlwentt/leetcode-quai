class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        answer = 0
        for num, count in counts.items():
            if count == 1:
                return - 1
            if count % 3 == 0:
                answer += count // 3
            else:        
                # count % 3 == 1 3+3+2+2  10
                # count % 3 == 2 3+3+3+2  11
                answer += count // 3 + 1
        return answer
        