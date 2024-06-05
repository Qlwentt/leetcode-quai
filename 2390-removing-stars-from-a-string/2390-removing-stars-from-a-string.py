class Solution:
    def removeStars(self, s: str) -> str:
        heap = []
        answer = list(s)
        for i, char in enumerate(s):
            if char == "*":
                j = heapq.heappop(heap)
                answer[-j] = ""
                answer[i] = ""
            else:
                heapq.heappush(heap, -i)
            
        return "".join(answer)