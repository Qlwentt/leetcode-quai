class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        j = 0
        answer = float('-inf')
        for i in range(0, len(tasks), 4):
            answer = max(tasks[i]+processorTime[j], answer)
            j += 1
        return answer
        
        # [8, 7, 5, 4, 3, 2, 2, 1]
        # [1, 2, 2, 3, 4, 5, 7, 8]
        # for i in range(len())
        
        