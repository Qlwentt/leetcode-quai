from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = [(-ord(char), count, char) for char, count in Counter(s).items() ]
        heapq.heapify(max_heap)
        
        answer = []
        
        while max_heap:
            weight, count, char = heapq.heappop(max_heap)
            if answer and answer[-1][-1] == char:
                continue
            times = min(count, repeatLimit)
            answer.append(times*char)
            left = count - times
            if left > 0 and max_heap:
                second_weight, second_count, second_char = heapq.heappop(max_heap)
                answer.append(second_char)
                second_count -= 1
                if second_count:
                    heapq.heappush(max_heap, (second_weight, second_count, second_char))
            if left > 0:
                heapq.heappush(max_heap, (weight, left, char))
        return "".join(answer)
            