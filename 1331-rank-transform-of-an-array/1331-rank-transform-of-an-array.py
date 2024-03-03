from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        numToI = defaultdict(list)
        
        for i, num in enumerate(arr):
            numToI[num].append(i)
            
        answer = [0] * len(arr)
        rank = 1
        for num in sorted(arr):
            answer[numToI[num].pop()] = rank
            if not numToI[num]:
                rank += 1
        
        return answer
            