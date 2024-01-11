class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxEle = -1
        answer = [-1] * len(arr)
        for i in range(len(answer)-2,-1,-1):
            maxEle = max(maxEle, arr[i+1])
            answer[i] = maxEle
        
        return answer
        