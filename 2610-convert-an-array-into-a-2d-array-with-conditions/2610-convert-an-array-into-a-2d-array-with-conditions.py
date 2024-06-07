class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = collections.Counter(nums)
        answer = []
        while len(counts):
            row = []
            curr = counts.copy()
            for num, count in counts.items():
                row.append(num)
                curr[num] -= 1
                if curr[num] == 0:
                    del curr[num]
            counts = curr
            answer.append(row)
        return answer
        