class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        while k:
            most_gifts = heapq.heappop(max_heap)
            heapq.heappush(max_heap,-math.floor(math.sqrt(-most_gifts)))
            k -= 1
        
        return -sum(max_heap)