from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        numToIndex = defaultdict(list)
        
        for i, num in enumerate(arr):
            numToIndex[num].append(i)
            
        arr.sort()
        answer = [0] * len(arr)
        rank = 1
        for i in range(len(arr)):
            for j in numToIndex[arr[i]]:
                answer[j] = rank
            if i+1 < len(arr) and  arr[i+1] != arr[i]:
                rank += 1
        return answer
        