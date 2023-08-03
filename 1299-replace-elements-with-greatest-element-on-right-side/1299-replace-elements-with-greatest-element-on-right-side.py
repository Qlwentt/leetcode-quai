class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prevMax = -1
        prev = -1
        for i in range(len(arr)-1, -1, -1):
            maxRight = max(prev, prevMax)
            prev = arr[i]
            prevMax = maxRight
            arr[i] = prevMax
        return arr