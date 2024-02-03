from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        numToIndices = defaultdict(list)
        
        for i, num in enumerate(arr):
            numToIndices[num].append(i)
            
        numKeys = sorted(numToIndices.keys())
        answer = [0]* len(arr)
        rank = 1
        for num in numKeys:
            for index in numToIndices[num]:
                answer[index] = rank
            rank += 1
        return answer
    
# Time: O(NlogN)
# Space: O(N)