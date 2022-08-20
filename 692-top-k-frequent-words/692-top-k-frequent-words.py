from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        maxHeap = [(-count, word) for word, count in counts.items()]
        heapq.heapify(maxHeap)
        
        answer = []
        while len(answer) < k:
            count, word = heapq.heappop(maxHeap)
            answer.append(word)
            
        return answer
        
        
            