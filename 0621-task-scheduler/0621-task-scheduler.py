from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [(-count, letter) for letter, count in counter.items()]
        heapq.heapify(heap)
        q = deque([]) # count, time, letter
        time = 0
        while heap or q:
            count, letter = heapq.heappop(heap) if heap else (-1, "")
            time += 1
            while q and q[0][2] <= time:
                unIdle = q.popleft()
                heapq.heappush(heap, (unIdle[0], unIdle[1]))
            count += 1
            if count:
                q.append((count, letter, time + n))
        return time             
            
            