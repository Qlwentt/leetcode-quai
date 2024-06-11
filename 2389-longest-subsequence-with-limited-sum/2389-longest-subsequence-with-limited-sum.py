class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            prefix_sums.append(cur_sum)
        answer = []
        for query in queries:
            a = bisect.bisect_right(prefix_sums, query)
            answer.append(a)
        return answer
        