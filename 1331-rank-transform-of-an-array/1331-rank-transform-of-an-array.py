from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        numToIndex = defaultdict(list)
        
        for i, num in enumerate(arr):
            numToIndex[num].append(i)
            
        arr.sort()
        answer = [0] * len(arr)
        rank = 1
        i = 0
        while i < len(arr):
            num = arr[i]
            for j in numToIndex[num]:
                answer[j] = rank
                i+=1
            rank += 1
        return answer
        