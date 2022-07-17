from collections import deque
class MaxHeap:
    def __init__(self, nums):
        self.heap = [ -x for x in nums]
        heapq.heapify(self.heap)
        
    def __str__(self):
        return ",".join(str(self.heap))
    
    def push(self, val):
        heapq.heappush(self.heap, val * -1)
        
    def pop(self):
        return heapq.heappop(self.heap) * -1
    
    def empty(self):
        return len(self.heap) == 0
    

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        
        maxHeap = MaxHeap(taskCount.values())
        
        q = deque([])
        time = 0
        while not maxHeap.empty() or q:
            time += 1
            
            if maxHeap.empty():
                time = q[0][1]
            else:
                task = maxHeap.pop()
                task -= 1
                if task:
                    cooldown = time + n
                    q.append((task, cooldown))

            if q and q[0][1] == time:
                task, cool = q.popleft()
                maxHeap.push(task)
        return time