from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        answer = [0]* len(arr)
        numToIndexes = defaultdict(list)
        
        for i, num in enumerate(arr):
            numToIndexes[num].append(i)
        
        rank = 1
        for num in sorted(numToIndexes):
            for i in numToIndexes[num]:
                answer[i] = rank
            rank += 1
            
        return answer
        
        