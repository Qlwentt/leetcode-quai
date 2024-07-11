class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        
        answer = -1
        
        for num in set(arr):
            if counts[num] == num:
                answer = max(num, answer)
        return answer