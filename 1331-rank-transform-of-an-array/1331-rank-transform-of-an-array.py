from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        numToIndex = defaultdict(list)
        
        for i, num in enumerate(arr):
            numToIndex[num].append(i)
            
        arr.sort()
        
        i = 0
        rank = 1
        answer = [0]*len(arr)
        while i < len(arr):
            num = arr[i]
            for j in numToIndex[num]:
                answer[j] = rank
                i += 1
            rank += 1
            
        return answer