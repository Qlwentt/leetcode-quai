class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = [-1] * len(arr)
        
        maxRight = -1
        for i in range(len(answer)-2,-1,-1):
            maxRight = max(maxRight, arr[i+1])
            answer[i] = maxRight
        return answer