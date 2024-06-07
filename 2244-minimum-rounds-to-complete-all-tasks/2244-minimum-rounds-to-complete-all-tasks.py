class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = collections.Counter(tasks)
        answer = 0
        
        for value, count in counts.items():
            if count == 1:
                return -1
            if count % 3 == 0:
                answer += count // 3
            else:
                answer += count // 3 + 1
        
        return answer
        